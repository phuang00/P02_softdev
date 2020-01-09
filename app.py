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
    if request.args:
        category1 = request.args.get('category1')
        db_functions.create_question(category1, request.args.get('q1'), request.args.get('a1'))
        return render_template('play.html', board_name = request.args.get('board_name'), q1 = request.args.get('c1q1'))
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
