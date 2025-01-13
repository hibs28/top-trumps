import requests
from pprint import pprint

# Ask for the Pokémon name
pokemon_name = input("What is the Pokémon's name? ").strip().lower()

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'

response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    pokemon = response.json()
    pprint(pokemon)
else:
    print(f"Error: Could not find Pokémon with name '{pokemon_name}'. Please check the spelling.")
