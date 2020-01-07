from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
import db_functions
import sqlite3  # enable control of an sqlite database
import os

app = Flask(__name__)  # create instance of class Flask
app.secret_key = os.urandom(24)
@app.route('/')
def index():
    # load the template with the user's session info
    if 'user' in session:
        return render_template('home.html')
    else: return render_template('base.html')


@app.route('/login')
def login():
    if 'user' in session:
        return render_template('home.html')
    elif request.args:
        if db_functions.checkfor_credentials(request.args.get('username'), request.args.get('password')):
            session['user'] = request.args.get('username')
            session['password'] = request.args.get('password')
            session['id'] = db_functions.get_user_id(request.args.get('username'))
            return render_template('home.html')
        else:
            flash('Invalid Credentials')
            return redirect(url_for('login'))
    else: return render_template('login.html')

@app.route('/register')
def register():
    if 'user' in session:
        return render_template('home.html')
    elif request.args:
        if db_functions.checkfor_username(request.args.get('username')):
            flash('Account with that username already exists')
            return redirect(url_for('register'))
        else:
            db_functions.create_user(request.args.get('username'), request.args.get('password'))
            flash('Account Created')
            return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == "__main__":
    app.debug = True
    app.run()