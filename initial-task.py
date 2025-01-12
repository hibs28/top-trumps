import requests

import random

from pprint import pprint

pokemon_number = random.randint(1, 151)
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()

print(response)
print(pokemon_number)

pokemon = response.json()
pprint(pokemon)

