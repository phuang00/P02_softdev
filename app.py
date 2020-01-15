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
        if request.args:
            categories = []
            for i in range(1, 6):
                cat = "c" + str(i)
                categories.append(request.args.get(cat))
            question_ids = []
            for c in categories:
                if c == 'pokemon':
                    for x in range(5):
                        question_ids.append(random.randrange(1, 25, 1))
                elif c == 'countries':
                    for x in range(5):
                        question_ids.append(random.randrange(26, 50, 1))
                elif c == 'rick_morty':
                    for x in range(5):
                        question_ids.append(random.randrange(51, 75, 1))
            #print(question_ids)
            db_functions.create_board(session['id'], request.args.get('board_name'), categories, question_ids)
            return redirect(url_for('home'))
        return render_template('create.html')
    return redirect(url_for('login'))

@app.route('/customize', methods=['GET', 'POST'])
def customize():
    if 'user' in session:
        if request.method =='POST':
            #print(request.form)
            question_ids = []
            categories = []
            for i in range(1, 6):
                cat = "c" + str(i)
                categories.append(request.form[cat])
                for j in range(1, 6):
                    question_ids.append(db_functions.create_question(request.form[cat], request.form[cat + "_q" + str(j)], request.form[cat + "_a" + str(j)]))
            print(categories)
            print(question_ids)
            db_functions.create_board(session['id'], request.form['board_name'], categories, question_ids)
            return redirect(url_for('home'))
        return render_template('customize.html')
    return redirect(url_for('login'))

@app.route('/play')
def play():
    if 'user' in session:
        if 'board_id' in request.args:
            board_id = request.args['board_id']
            user_id = session['id']
            board_id = db_functions.get_board_id(user_id, board_name)
            session['board_id'] = board_id
            categories = db_functions.get_board_categories(user_id, board_id)
            #print(board_id)
            #print(categories)
            session['game_id'] = db_functions.create_game(board_id, categories)
            return render_template('play.html')
        elif 'team1' in request.args:
            #Add teams to database
            x = 1;
            while 'team' + str(x) in request.args:
                db_functions.create_team(session['game_id'], request.args.get('team' + str(x)))
                x += 1
            #Getting array of questions
            categories = db_functions.get_board_categories(session['id'], session['board_id'])
            question_ids = db_functions.get_board_question_ids(session['board_id'])
            questions = db_functions.get_board_questions(question_ids)
            questions.insert(0, categories[0])
            questions.insert(11, categories[1])
            questions.insert(22, categories[2])
            questions.insert(33, categories[3])
            questions.insert(44, categories[4])
            #Format of questions array: category, q1, a1, q2, a2, q3, a3, q4, a4, q5, a5, ...
            return render_template('game.html')
        return redirect(url_for('board'))
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
    create_db.add_questions()
    app.debug = True
    app.run()
