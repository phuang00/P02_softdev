import os
import json
import urllib
import random
import urllib.request

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

    return

# OPEN TRIVIA API
def getOpenTrivia():
    pop = urllib.request.urlopen("https://opentdb.com/api.php?amount=25")
    # so far only has one set of questions
    data = [json.loads(pop.read())]
    m = 24;
    d = []
    while m >= 0:
        d.append(data[0]['results'][m]['question'])
        d.append(data[0]['results'][m]['correct_answer'])
        m = m - 1

    return

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

    print(d)

    return

getRickAndMorty()
