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
    create_table_board = "CREATE TABLE IF NOT EXISTS board(board_id INTEGER, user_id INTEGER, board_name TEXT, category TEXT, q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER);"
    insert_dummy = "INSERT OR IGNORE INTO board(board_id) VALUES(0)"
    create_table_teams = "CREATE TABLE IF NOT EXISTS teams(game_id INTEGER, team_name TEXT, score INTEGER);"
    create_table_board_status = "CREATE TABLE IF NOT EXISTS board_status(board_id INTEGER, game_id INTEGER, category TEXT, q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER);"
    create_table_questions = "CREATE TABLE IF NOT EXISTS questions(question_id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, question TEXT, answer TEXT);"

    c.execute(create_table_users)
    c.execute(insert_user)
    c.execute(create_table_board)
    c.execute(insert_dummy)
    c.execute(create_table_teams)
    c.execute(create_table_board_status)
    c.execute(create_table_questions)

    db.commit()  # save changes
    db.close()  # close database

def add_questions():
    #Adding Pokemon questions
    pokemon_num = db_functions.category_size('pokemon')
    if pokemon_num < 25:
        poke_questions = api.getPokemon()
        #print(poke_questions)
        x = 2 * pokemon_num;
        while x < 50:
            db_functions.create_question('pokemon', poke_questions[x], poke_questions[x+1])
            x += 2

    #Adding countries questions
    countries_num = db_functions.category_size('countries')
    if countries_num < 25:
        country_questions = api.getCountries()
        x = 2 * countries_num;
        while x < 50:
            db_functions.create_question('countries', country_questions[x], country_questions[x+1])
            x += 2

    rick_morty_num = db_functions.category_size('rick_morty')
    if rick_morty_num < 25:
        rick_morty_questions = api.getRickAndMorty()
        #print(rick_morty_questions)
        x = 2 * rick_morty_num;
        while x < 50:
            db_functions.create_question('rick_morty', rick_morty_questions[x], rick_morty_questions[x+1])
            x += 2

    history_num = db_functions.category_size('history')
    if history_num < 25:
        history_questions = api.getHistory()
        #print(rick_morty_questions)
        x = 2 * history_num;
        while x < 50:
            db_functions.create_question('history', history_questions[x], history_questions[x+1])
            x += 2

    science_num = db_functions.category_size('science')
    if science_num < 25:
        science_questions = api.getScience()
        #print(rick_morty_questions)
        x = 2 * science_num;
        while x < 50:
            db_functions.create_question('science', science_questions[x], science_questions[x+1])
            x += 2

    film_num = db_functions.category_size('film')
    if film_num < 25:
        film_questions = api.getFilm()
        #print(rick_morty_questions)
        x = 2 * film_num;
        while x < 50:
            db_functions.create_question('film', film_questions[x], film_questions[x+1])
            x += 2

    animals_num = db_functions.category_size('animals')
    if animals_num < 20:
        animals_questions = api.getAnimals()
        #print(rick_morty_questions)
        x = 2 * animals_num;
        while x < 40:
            db_functions.create_question('animals', animals_questions[x], animals_questions[x+1])
            x += 2
