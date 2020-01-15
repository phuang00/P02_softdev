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
        d.append(data[0][y]['name'])
        x = x - 1
    return d

# OPEN TRIVIA API
def getHistory():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=25&category=23&type=boolean")
    # so far only has one set of questions
    data = [json.loads(pop.read())]
    m = 24;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append(data[0]['results'][m]['correct_answer'])
        m = m - 1
    return d

def getAnimals():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=20&category=27&type=boolean")
    # so far only has one set of questions
    data = [json.loads(pop.read())]
    m = 19;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append(data[0]['results'][m]['correct_answer'])
        m = m - 1
    return d

def getScience():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=25&category=17&type=boolean")
    # so far only has one set of questions
    data = [json.loads(pop.read())]
    m = 24;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append(data[0]['results'][m]['correct_answer'])
        m = m - 1
    return d

def getFilm():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=25&category=11&type=boolean")
    # so far only has one set of questions
    data = [json.loads(pop.read())]
    m = 24;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append(data[0]['results'][m]['correct_answer'])
        m = m - 1
    return d

# RICK AND MORTY API
def getRickAndMorty():
    pop = urllib.request.urlopen("https://rickandmortyapi.com/api/character")
    data = [json.loads(pop.read())]
    n = 19
    d = []
    while n >= 0:
        # question
        d.append(data[0]['results'][n]['image'])
        # answer
        d.append(data[0]['results'][n]['name'])
        n = n - 1
    rick = urllib.request.urlopen("https://rickandmortyapi.com/api/character/?page=2")
    morty = [json.loads(rick.read())]
    l = 0
    while l < 5:
        y = random.randint(-1,19)
        # question
        d.append(data[0]['results'][n]['image'])
        # answer
        d.append(data[0]['results'][n]['name'])
        l = l + 1
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
        d.append(data['results'][m]['name'])
        m = m - 1
    return d
