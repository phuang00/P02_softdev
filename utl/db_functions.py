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
    c.execute(query)
    response = c.fetchone()[0]
    db.commit()  # save changes
    db.close()  # close database
    return response

def get_board_id(user_id, board_name):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT board_id FROM board WHERE user_id == \"%s\" AND board_name == \"%s\";" % (user_id, board_name)
    c.execute(query)
    response = c.fetchone()[0]
    db.commit()  # save changes
    db.close()  # close database
    return response

def get_board_categories(user_id, board_name):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT category FROM board WHERE user_id == \"%s\" AND board_name == \"%s\";" % (user_id, board_name)
    c.execute(query)
    data = []
    for row in c.fetchall():
        data.append(row[0])
    db.commit()  # save changes
    db.close()  # close database
    return data

# Gets the highest id currently in a table column
def get_highest_num(table, col):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops
    query = "SELECT MAX(%s) FROM %s;" % (col, table)
    c.execute(query)
    response = c.fetchone()[0]
    if response == None:
        response = 0
    db.commit()  # save changes
    db.close()  # close database
    return response

#Finds how many questions are in a category
def category_size(category):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops
    query = "SELECT COUNT(*) FROM questions WHERE questions.category = \"%s\";" % (category)
    c.execute(query)
    response = c.fetchone()[0]
    db.commit()  # save changes
    db.close()  # close database
    return response

def create_question(category, question, answer):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops
    #IF NOT EXISTS (SELECT * FROM questions WHERE question=question)
    #if (NOT EXISTS (SELECT * FROM questions WHERE question = question2)):
    #    query = "INSERT INTO questions(category, question, answer) VALUES(\"%s\", \"%s\", \"%s\");" % (category, question2, answer)
    #    response = list(c.execute(query))
    #    db.commit()  # save changes
    #    db.close()  # close database

    query = "INSERT INTO questions(category, question, answer) VALUES(\"%s\", \"%s\", \"%s\");" % (category, question, answer)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database
    id = get_highest_num('questions', 'question_id')
    return id

def create_game(board_id, categoryList):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    i = 0
    while i < 5:
        query = "INSERT INTO board_status(board_id, category, q1, q2 ,q3 ,q4 ,q5) VALUES(\"%s\", \"%s\", 1, 1, 1, 1, 1)" % (board_id, categoryList[i])
        response = list(c.execute(query))
        i += 1
    db.commit()
    db.close()
    return response

def create_board(user_id, board_name, categories, question_ids):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    i = 0
    board_id = get_highest_num("board", "board_id") + 1
    while i < 5:
        c.execute("INSERT INTO board(board_id, user_id, board_name, category, q1, q2, q3, q4, q5) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);",
                  (board_id, user_id, board_name, categories[i], question_ids[i * 5], question_ids[i * 5 + 1],
                   question_ids[(i * 5 + 2)], question_ids[i * 5 + 3], question_ids[i * 5 + 4],))
        i = i + 1
    db.commit()
    db.close()

#create_board(2,"s","s",[2,4,3,5,3,5,3,3,5,4])

def add_flag_questions(flag_list):
    i = 0
    while i < len(flag_list):
        create_question("geography",flag_list[i],flag_list[i+1])
        i += 2

def add_RM_questions(character_list):
    i = 0
    while i < len(character_list):
        create_question("Rick and Morty",character_list[i],character_list[i+1])
        i += 2

def add_pokemon_questions(pokemon_list):
    i = 0
    while i < len(pokemon_list):
        create_question("Pokemon",pokemon_list[i],pokemon_list[i+1])
        i += 2

def add_general_questions(question_list):
    i = 0
    while i < len(question_list):
        create_question("General Knowledge",question_list[i],question_list[i+1])
        i += 2

# create_question("GEN","hithere","hello")
# create_question("GEN","hithere","hello")

def get_games(username):
    history = []
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT DISTINCT board_name FROM board, users WHERE username = ? AND board.user_id == users.user_id;", (username,))
    for row in c.fetchall():
        history.append(row[0])
    return history

def search_board(name):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT DISTINCT board_name FROM board WHERE board_name LIKE '%' || ? || '%';", (name,))
    data = []
    for row in c.fetchall():
        data.append(row[0])
    db.commit()
    db.close()
    return data
