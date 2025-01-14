import requests
import random

#generate a random number between 1 and 151
pokemon_number = random.randint(1, 151)
opponent_number = random.randint(1, 151)

#function to retrieve Pokémon data for Player 1
def retrieve_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()

    else:
        print(f"Error: Could not find Pokémon with this ID '{pokemon_number}'. Please check the number.")
        return None

#Function to call types for pokemon
def retrieve_by_type(pokemon_type):
    pokemon_type_url = 'https://pokeapi.co/api/v2/type/{}'.format(pokemon_type)
    return requests.get(pokemon_type_url).json()

# Retrieves weight from API GET response and converts it from hectograms to kilograms.
def weight_retrieval(pokemon):
    weight = pokemon['weight']
    weight = int(weight) / 10
    print("Pokémon Weight: " + str(weight) + "kg")

# Retrieves name of Pokémon
def name_retrieval(pokemon):
    name = pokemon['name'].title()
    print("Pokémon Name: " + name)

# Height is in Centimetres
def height_retrieval(pokemon):
    height = pokemon['height']
    height = int(height) * 10
    print("Pokémon Height: " + str(height) + "cm")

#Gets a list of pokemon types from API call
def get_pokemon_type_list():
    pokemon_response = retrieve_by_type("")
    pokemon_type_list = []
    for pokemon_type in pokemon_response['results']:
        pokemon_type_list.append(pokemon_type['name'])
    print("\nList of pokemon types: " + str(pokemon_type_list))



pokemon = retrieve_pokemon_data(pokemon_number)
opponent = retrieve_pokemon_data(opponent_number)


# Player 1 Data
if pokemon:
    print("\nPokémon ID: " + str(pokemon_number))
    name_retrieval(pokemon)
    height_retrieval(pokemon)
    weight_retrieval(pokemon)

   #Dictionary for Player 1's Pokémon
    pokemon_dict = {'id':pokemon_number,
                   'name':pokemon['name'],
                   'height':pokemon['height'],
                   'weight':pokemon['weight']
                   }

    print("Player's Pokémon Dictionary" + str(pokemon_dict))

else:
    print("Error fetching Player's Pokémon data.\n")


#retrieving opponent's data
if opponent:
    print("\nOpponent Pokémon ID: " + str(opponent_number))
    opponent_name = opponent['name'].title()
    print("Opponent Pokémon Name: " + opponent_name)
    opponent_height = int(opponent['height']) * 10  # Height in cm
    print("Opponent Pokémon Height: " + str(opponent_height) + "cm")
    opponent_weight = int(opponent['weight']) / 10  # Weight in kg
    print("Opponent Pokémon Weight: " + str(opponent_weight) + "kg")

## Create dictionary for the opponent's Pokémon
    opponent_dict = {
        'id': opponent_number,
        'name': opponent['name'],
        'height': opponent['height'],
        'weight': opponent['weight']
    }
    print("Opponent's Pokémon Dictionary:", opponent_dict)
else:
    print("Error fetching Opponent's Pokémon data.\n")

#Battle mode for type
def battle_by_type():
    type_one = get_by_type('electric')
    type_two = 'fire'

    damage_to_list = []
    for i in type_one['damage_relations']['double_damage_to']:
        damage_to_list.append(i['name'])

    for i in type_one['damage_relations']['half_damage_to']:
        damage_to_list.append(i['name'])
    print('\n=======================  BATTLE  MODE  =======================')
    print('\nTypes that damage water type pokemon: ' + str(damage_to_list))
    if type_two in damage_to_list:
        print("You have WON!")
    else: print("Sorry you lost.")


# Ask the player to choose a stat
stat_choice = input("\nChoose a stat to compare (height, weight): ").lower()

if stat_choice not in ['height', 'weight']:
    print("Invalid choice. Please choose either 'height', or 'weight'.")

else:
    #Compare the stats of the Player 1 and Opponent
    def compare_stat(pokemon_dict,opponent_dict, stat_choice):
        pokemon_stat = pokemon_dict[stat_choice]
        opponent_stat = opponent_dict[stat_choice]

        print(f"Player's {stat_choice}: {pokemon_stat}")
        print(f"Opponent's {stat_choice}: {opponent_stat}")


        if pokemon_stat > opponent_stat:
            return "Player 1 wins!"

        elif opponent_stat > pokemon_stat:
            return 'Opponent wins!'

        else:
            return "It's a draw!"


    #Call compare_stat function and print the result
    result = compare_stat(pokemon_dict, opponent_dict, stat_choice)
    print(result)
