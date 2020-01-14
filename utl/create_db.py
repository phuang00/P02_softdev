import sqlite3  # enable control of an sqlite database
from utl import api, db_functions

DB_FILE = "jeopardy.db"

def create():
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops


    # < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

    #==========================================================

    # test SQL stmt in sqlite3 shell, save as string
    create_table_users = "CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT);"
    insert_user = "INSERT OR IGNORE INTO users(user_id, username, password) VALUES( 1, \"admin\", \"peterstuy\");"
    create_table_board = "CREATE TABLE IF NOT EXISTS board(board_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, board_name TEXT, category TEXT, q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER);"
    create_table_teams = "CREATE TABLE IF NOT EXISTS teams(game_id INTEGER PRIMARY KEY AUTOINCREMENT, team_name TEXT, score INTEGER);"
    create_table_board_status = "CREATE TABLE IF NOT EXISTS board_status(board_id INTEGER PRIMARY KEY, category TEXT, q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER);"
    create_table_questions = "CREATE TABLE IF NOT EXISTS questions(question_id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, question TEXT, answer TEXT);"

    c.execute(create_table_users)
    c.execute(insert_user)
    c.execute(create_table_board)
    c.execute(create_table_teams)
    c.execute(create_table_board_status)
    c.execute(create_table_questions)

    db.commit()  # save changes
    db.close()  # close database

def add_questions():
    poke_questions = api.getPokemon()
    #print(poke_questions)
    x = 0;
    while x < 50:
        db_functions.create_question('pokemon', poke_questions[x], poke_questions[x+1])
        x += 2
        print(x)
