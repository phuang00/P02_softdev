import sqlite3  # enable control of an sqlite database

DB_FILE = "jeopardy.db"
# checkfor_credentials()
# - @return username and password of accounts that meet the credentials in the password (either an empty touple or 1-sized touple)
def checkfor_credentials(username, password):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT username, password FROM users WHERE users.username = \"%s\" AND users.password = \"%s\";" % (username, password)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

    return response


def checkfor_username(username):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT username FROM users WHERE username == \"%s\";" % (username)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

    return response


def create_user(username, password):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "INSERT INTO users(username, password) VALUES(\"%s\", \"%s\");" % (username, password)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

    return response

def get_user_id(username):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT user_id FROM users WHERE username == \"%s\";" % (username)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database
    return response

# Gets the highest id currently in a table column
def get_highest_num(table, col):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops
    query = "SELECT MAX(%s) FROM %s;" % (col, table)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database
    print(response)
    return response

def create_question(category, question, answer):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "INSERT INTO questions(category, question, answer) VALUES(\"%s\", \"%s\", \"%s\");" % (category, question, answer)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

    return response

def create_board(categoryList):
    i = 0
    while i < 5:
        query = "INSERT INTO board_status(category, q1, q2 ,q3 ,q4 ,q5) VALUES(\"%s\", 1, 1, 1, 1, 1)" % (categoryList[0])
        response = list(c.execute(query))
        i += 1
    db.commit()
    db.close()
    return response
