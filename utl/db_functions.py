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

def get_board_name(board_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT board_name FROM board WHERE board_id == \"%s\";" % (board_id)
    c.execute(query)
    response = c.fetchone()[0]
    db.commit()  # save changes
    db.close()  # close database
    return response

def get_board_id(game_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT board_id FROM board_status WHERE game_id == \"%s\";" % (game_id)
    c.execute(query)
    response = c.fetchone()[0]
    db.commit()  # save changes
    db.close()  # close database
    return response

def get_board_categories(user_id, board_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT category FROM board WHERE user_id == \"%s\" AND board_id == \"%s\";" % (user_id, board_id)
    c.execute(query)
    data = []
    for row in c.fetchall():
        data.append(row[0])
    db.commit()  # save changes
    db.close()  # close database
    return data

def get_board_question_ids(board_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT * FROM board WHERE board_id == \"%s\";" % (board_id)
    c.execute(query)
    data = []
    for row in c.fetchall():
        data.append(row[5])
        data.append(row[6])
        data.append(row[7])
        data.append(row[8])
        data.append(row[9])
    db.commit()  # save changes
    db.close()  # close database
    return data

def get_board_questions(question_ids):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops
    data = []

    for q in question_ids:
        query = "SELECT question, answer FROM questions WHERE question_id == \"%s\";" % (q)
        c.execute(query)
        for row in c.fetchall():
            data.append(row[0])
            data.append(row[1])
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

def create_game(user_id, board_id, categoryList):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    game_id = get_highest_num('board_status', 'game_id') + 1
    i = 0
    while i < 5:
        #query = "INSERT INTO board_status(board_id, category, q1, q2 ,q3 ,q4 ,q5) VALUES(\"%s\", \"%s\", 1, 1, 1, 1, 1)" % (board_id, categoryList[i])
        c.execute("INSERT INTO board_status(user_id, board_id, game_id, row, category, q1, q2 ,q3 ,q4 ,q5) VALUES(?, ?, ?, ?, ?, 1, 1, 1, 1, 1)", (user_id, board_id, game_id, i, categoryList[i]))
        i += 1
    db.commit()
    db.close()
    return game_id

def get_board_status(game_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT * FROM board_status WHERE game_id == \"%s\";" % (game_id)
    c.execute(query)
    data = []
    for row in c.fetchall():
        data.append(row[5])
        data.append(row[6])
        data.append(row[7])
        data.append(row[8])
        data.append(row[9])
    db.commit()  # save changes
    db.close()  # close database
    return data

def create_board(user_id, board_name, categories, question_ids):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    i = 0
    board_id = get_highest_num("board", "board_id") + 1
    while i < 5:
        print(i)
        c.execute("INSERT INTO board(board_id, user_id, board_name, row, category, q1, q2, q3, q4, q5) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                  (board_id, user_id, board_name, i, categories[i], question_ids[i * 5], question_ids[i * 5 + 1],
                   question_ids[(i * 5 + 2)], question_ids[i * 5 + 3], question_ids[i * 5 + 4],))
        i = i + 1
    db.commit()
    db.close()

def create_team(game_id, team_name, turn):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "INSERT INTO teams(game_id, team_name, turn, score) VALUES(\"%s\", \"%s\", \"%s\", 0);" % (game_id, team_name, turn)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

    return response

def get_teams(game_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT team_name FROM teams WHERE game_id == \"%s\";" % (game_id)
    c.execute(query)
    data = []
    for row in c.fetchall():
        data.append(row[0])
    db.commit()  # save changes
    db.close()  # close database
    return data

def get_turn(game_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT team_name FROM teams WHERE game_id == \"%s\" AND turn == 1;" % (game_id)
    c.execute(query)
    response = c.fetchone()[0]
    db.commit()  # save changes
    db.close()  # close database
    return response

def update_turn(game_id, old_team, new_team):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    #query = "UPDATE teams SET turn = 0 WHERE game_id == \"%s\" AND team_name == \"%s\";" % (game_id, old_team)
    #c.execute(query)
    #query = "UPDATE teams SET turn = 1 WHERE game_id == \"%s\" AND team_name == \"%s\";" % (game_id, new_team)
    #c.execute(query)
    c.execute("UPDATE teams SET turn=0 WHERE game_id=? AND team_name=?", (game_id, old_team))
    c.execute("UPDATE teams SET turn=1 WHERE game_id=? AND team_name=?", (game_id, new_team))
    db.commit()  # save changes
    db.close()  # close database
    return

def get_boards(username):
    history = {}
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT DISTINCT board_name, board_id FROM board, users WHERE username = ? AND board.user_id == users.user_id;", (username,))
    for row in c.fetchall():
        history[row[0]] = row[1]
    return history

def search_board(name):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT DISTINCT board_name, board_id FROM board WHERE board_name LIKE '%' || ? || '%';", (name,))
    data = {}
    for row in c.fetchall():
        data[row[0]] = row[1]
    db.commit()
    db.close()
    return data

def add_score(id,team,score_added):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE teams SET score=score+ ? WHERE game_id=? AND team_name=?", (score_added,id,team,))
    db.commit()
    db.close()

def mark_question_done(game_id, q_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    row = (q_id - 1) // 5
    if q_id % 5 == 0:
        col = "q5"
    else:
        col = "q" + str(q_id % 5)
    query = "UPDATE board_status SET \"%s\"=0 WHERE game_id=\"%s\" AND row=\"%s\";" % (col,game_id,row)
    #print(query)
    c.execute(query)
    db.commit()
    db.close()

def check_if_finished(game_id):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT q1, q2, q3, q4, q5 FROM board_status WHERE game_id == \"%s\";" % (game_id)
    c.execute(query)
    data = []
    for row in c.fetchall():
        data.append(row[0])
        data.append(row[1])
        data.append(row[2])
        data.append(row[3])
        data.append(row[4])
    db.commit()  # save changes
    db.close()  # close database
    for x in data:
        if x == 1:
            return False
    return True

def get_games(user_id):
    games = {}
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT DISTINCT board_name, game_id FROM board, board_status, users WHERE board.board_id == board_status.board_id AND board_status.user_id == ?;", (user_id,))
    for row in c.fetchall():
        games[row[0]] = row[1]
    return games

def get_score(game_id):
    scores = []
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

   #query = "SELECT score FROM teams WHERE game_id == \"%s\" AND team_name == \"%s\";"  % (game_id,team_name)
    query = "SELECT score FROM teams WHERE game_id == \"%s\";"  % (game_id)
    c.execute(query)
    #response = c.fetchall()[0]
    for score in c.fetchall():
        scores.append(score[0])
    #print(scores)
    db.commit()  # save changes
    db.close()  # close database
    return scores
