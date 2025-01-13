import requests

import random

from pprint import pprint

pokemon_number = random.randint(1, 151)
#generate a random number between 1 and 151

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()

print(response)
print(pokemon_number)

pokemon = response.json()
pprint(pokemon)

# Retrieves weight from API GET response and converts it from hectograms to kilograms.
def convert_to_kg(pokemon):
    weight = pokemon['weight']
    weight = int(weight) / 10
    print(str(weight) + "kg")

convert_to_kg(pokemon)
