import os
import json
import urllib
import random
import urllib.request
from urllib.request import Request, urlopen

# COUNTRIES API
def getCountries():
    pop = urllib.request.urlopen("https://restcountries.eu/rest/v2/")
    data = [json.loads(pop.read())]
    x = 25
    d = []
    # Random countries and flags
    while x > 0:
        y = random.randint(-1,249)
        # question
        d.append(data[0][y]['flag'])
        # answer
        d.append('What is ' + data[0][y]['name'] + '?')
        x = x - 1
    return d

# OPEN TRIVIA API
def getHistory():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=25&category=23&type=boolean")
    data = [json.loads(pop.read())]
    m = 24;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append('What is ' + data[0]['results'][m]['correct_answer'] + '?')
        m = m - 1
    return d

def getAnimals():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=20&category=27&type=boolean")
    data = [json.loads(pop.read())]
    m = 19;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append('What is ' + data[0]['results'][m]['correct_answer'] + '?')
        m = m - 1
    return d

def getScience():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=25&category=17&type=boolean")
    data = [json.loads(pop.read())]
    m = 24;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append('What is ' + data[0]['results'][m]['correct_answer'] + '?')
        m = m - 1
    return d

def getFilm():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=25&category=11&type=boolean")
    data = [json.loads(pop.read())]
    m = 24;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append('What is ' + data[0]['results'][m]['correct_answer'] + '?')
        m = m - 1
    return d

# RICK AND MORTY API
def getRickAndMorty():
    a = 1;
    allCharacters = []
    while a <= 5:
        pop = urllib.request.urlopen("https://rickandmortyapi.com/api/character/?page=" + str(a))
        data = [json.loads(pop.read())]
        n = 19
        while n >= 0:
            # question
            allCharacters.append(data[0]['results'][n]['image'])
            # answer
            allCharacters.append('Who is ' + data[0]['results'][n]['name'] + '?')
            n = n - 1
        a = a + 1
    """ Method for preventing duplicates """
    dummy = 100
    randNums = []
    while dummy >= 0:
        randNums.append(dummy)
        dummy = dummy - 1
    size = 100
    numQuestions = 25
    d = []
    while numQuestions > 0:
        index = random.randint(-1,size)
        y = randNums[index]
        if y % 2 == 0:
            d.append(allCharacters[y])
            d.append(allCharacters[y+1])
            allCharacters.pop(y)
            allCharacters.pop(y)
        if y % 2 == 1:
            d.append(allCharacters[y-1])
            d.append(allCharacters[y])
            allCharacters.pop(y)
            allCharacters.pop(y-1)
        randNums.pop(index)
        size = size - 1
        numQuestions = numQuestions - 1
    return d

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

# POKE API
def getPokemon():
    request = Request("https://pokeapi.co/api/v2/pokemon/?offset=100&limit=100", headers=headers)
    response = urlopen(request).read()
    data = json.loads(response)
    m = 25
    d = []
    while m >= 0:
        # question
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        monpics = [json.loads(mon)]
        d.append(monpics[0]['sprites']['front_default'])
        # answer
        d.append('Who is ' + data['results'][m]['name'] + '?')
        m = m - 1
    return d
