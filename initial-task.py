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

# Retrieves weight from API GET response and converts it from hectograms to kilograms.
def convert_to_kg(pokemon):
    weight = pokemon['weight']
    weight = int(weight) / 10
    print(str(weight) + "kg")

def name_retrieval(pokemon):
    name = pokemon['name']
    print("What is the Pokémon's name? " + name)

# Check if the response is successful
if response.status_code == 200:
    pokemon = response.json()
    # pprint(pokemon)
    name_retrieval(pokemon)
    convert_to_kg(pokemon)

else:
    print(f"Error: Could not find Pokémon with this ID '{pokemon_number}'. Please check the number.")
