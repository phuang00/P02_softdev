import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O

DB_FILE = "jeopardy.db"

def create():
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops


    # < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

    #==========================================================

    # test SQL stmt in sqlite3 shell, save as string
    create_table_users = "CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT);"
    insert_user = "INSERT OR IGNORE INTO users(user_id, username, password) VALUES( 1, \"admin\", \"peterstuy\");"
    c.execute(create_table_users)
    c.execute(insert_user)

    db.commit()  # save changes
    db.close()  # close database
