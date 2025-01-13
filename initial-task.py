import requests

import random

from pprint import pprint

pokemon_number = random.randint(1, 151)
#generate a random number between 1 and 151

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()

print(response)
print("Pokémon ID: " + str(pokemon_number))

# Retrieves weight from API GET response and converts it from hectograms to kilograms.
def weight_retrieval(pokemon):
    weight = pokemon['weight']
    weight = int(weight) / 10
    print("Pokémon Weight: " + str(weight) + "kg")

def name_retrieval(pokemon):
    name = pokemon['name'].title()
    print("Pokémon Name: " + name)

# Height is in Centimetres
def height_retrieval(pokemon):
    height = pokemon['height']
    height = int(height) * 10
    print("Pokémon Height: " + str(height) + "cm")

# Check if the response is successful
if response.status_code == 200:
    pokemon = response.json()
    # pprint(pokemon)
    name_retrieval(pokemon)
    height_retrieval(pokemon)
    weight_retrieval(pokemon)  

else:
    print(f"Error: Could not find Pokémon with this ID '{pokemon_number}'. Please check the number.")
