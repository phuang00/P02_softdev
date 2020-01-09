from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
from utl import db_functions, create_db
import sqlite3  # enable control of an sqlite database
import os
import json
import urllib
import random

app = Flask(__name__)  # create instance of class Flask
app.secret_key = os.urandom(24)
@app.route('/')
def index():
    # load the template with the user's session info
    if 'user' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/login')
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.args:
        if db_functions.checkfor_credentials(request.args.get('username'),
                                             request.args.get('password')):
            session['user'] = request.args.get('username')
            session['password'] = request.args.get('password')
            session['id'] = db_functions.get_user_id(request.args.get('username'))
            return redirect(url_for('home'))
        flash('Invalid Credentials')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register')
def register():
    if 'user' in session:
        return render_template('home.html')
    elif request.args:
        if db_functions.checkfor_username(request.args.get('username')):
            flash('Account with that username already exists')
            return redirect(url_for('register'))
        db_functions.create_user(request.args.get('username'), request.args.get('password'))
        flash('Account Created')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html', user = session['user'])
    return redirect(url_for('login'))

@app.route('/board')
def board():
    if 'user' in session:
        return render_template('board.html')
    return redirect(url_for('login'))

@app.route('/create')
def create():
    if 'user' in session:
        return render_template('create.html')
    return redirect(url_for('login'))

@app.route('/customize')
def customize():
    if 'user' in session:
        return render_template('customize.html')
    return redirect(url_for('login'))

@app.route('/play')
def play():
    if 'user' in session:

        # COUNTRIES API
        pop = urllib.request.urlopen("https://restcountries.eu/rest/v2/")
        data = [json.loads(pop.read())]
        x = 25
        h = 25
        d = ""
        # Random countries and flags
        while x > 0:
            y = random.randint(-1,249)
            d = d + data[0][y]['name'] + " "
            # line to append to database, gets random country
            pics = data[0][y]['flag']
            # line to append to database, gets corresponding flag
            x = x - 1

        # RICK AND MORTY API
        rick = urllib.request.urlopen("https://rickandmortyapi.com/api/character")
        morty = [json.loads(rick.read())]
        n = 25
        # Random character images and names
        while n > 0:
            p = random.randint(-1,19)
            pic = morty[0]['results'][p]['image']
            # line to append to database, gets random image
            name = morty[0]['results'][0]['name']
            # line to append to database, gets random name
            n = n - 1

        # POKE API (doesn't work idk whyyyyy)
        #poke = urllib.request.urlopen("https://pokeapi.co/api/v2/pokemon/")
        #mon = [json.loads(poke.read())]
        #m = 25
        #q = mon[0]['results'][0]['url']
        #w = urllib.request.urlopen(q)
        #monpics = [json.loads(v.read())]
        #picz = monpics[0]['sprites']['front_default']

        # OPEN TRIVIA API  ( requires a session token, they expire after six hours )
        trivia = urllib.request.urlopen("https://opentdb.com/api.php?amount=25")
        questions = [json.loads(trivia.read())]
        m = 0;
        while m <= 25:
            question = questions[m]['results'][m]['question']
            # line append question to database
            answer = questions[m]['results'][m]['correct_answer']
            # line to append answer to database
            m += 1
            
        return render_template('play.html', board_name = request.args.get('board_name'))
    return redirect(url_for('login'))

@app.route('/search')
def search():
    if 'user' in session:
        return render_template('search.html', search = request.args.get('keyword'))
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged Out Succesfully")
    return redirect(url_for("index"))

if __name__ == "__main__":
    create_db.create()
    app.debug = True
    app.run()
