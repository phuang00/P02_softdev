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
        return render_template('home.html', user = session['user'], games=db_functions.get_games(session['user']))
    return redirect(url_for('login'))

@app.route('/board')
def board():
    if 'user' in session:
        return render_template('board.html')
    return redirect(url_for('login'))

@app.route('/create')
def create():
    if 'user' in session:
        return render_template('create.html', board_name = request.args.get('board_name'))
    return redirect(url_for('login'))

@app.route('/customize', methods=['GET', 'POST'])
def customize():
    if 'user' in session:
        if request.method =='POST':
            #print(request.form)
            question_ids = []
            category1 = request.form['c1']
            q_num = db_functions.create_question(category1, request.form['c1_q1'], request.form['c1_a1'])
            print(q_num[0][0])
            question_ids.append(q_num)
            return redirect(url_for('home'))
        return render_template('customize.html')
    return redirect(url_for('login'))

@app.route('/play')
def play():
    if 'user' in session:
        return render_template('play.html')
    return redirect(url_for('login'))

@app.route('/search')
def search():
    if 'user' in session:
        result = []
        if 'keyword' in request.args:
            keyword = request.args['keyword']
            result = db_functions.search_board(keyword)
            return render_template('search.html', results=result, search=keyword)
        return render_template('search.html', results=result, search="")
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
