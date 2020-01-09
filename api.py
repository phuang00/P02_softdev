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
    print(d)
    return


getCountries()
