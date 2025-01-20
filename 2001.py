import random
import requests

from final import opponent_weight

# generate a random number between 1 and 151
pokemon_number = random.randint(1, 151)
opponent_number = random.randint(1, 151)

player_one_wins = 0
opponent_wins = 0

my_string = r"""
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
"""

print(my_string)


# function to retrieve Pokémon data for Player 1
def retrieve_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()

    else:
        print(f"Error: Could not find Pokémon with this ID '{pokemon_number}'. Please check the number.")
        return None


# Function to call types for pokemon
def retrieve_by_type(pokemon_type):
    pokemon_type_url = 'https://pokeapi.co/api/v2/type/{}'.format(pokemon_type)
    return requests.get(pokemon_type_url).json()


# Retrieves weight from API GET response and converts it from hectograms to kilograms.
def weight_retrieval(pokemon):
    weight = pokemon['weight']
    weight = int(weight) / 10
    print("Player One Pokémon Weight: " + str(weight) + "kg")
    return weight


# Retrieves name of Pokémon
def name_retrieval(pokemon):
    name = pokemon['name'].title()
    print("Player One Pokémon Name: " + name)



# Height is in Centimetres
def height_retrieval(pokemon):
    height = pokemon['height']
    height = int(height) * 10
    print("Player One Pokémon Height: " + str(height) + "cm")
    return height


def type_retrieval(pokemon):
    type_pokemon = pokemon['types'][0]['type']['name'].title()
    print("Player One Pokémon Type: " + type_pokemon)


# Gets a list of pokemon types from API call
def get_pokemon_type_list():
    pokemon_response = retrieve_by_type("")
    pokemon_type_list = []
    for pokemon_type in pokemon_response['results']:
        pokemon_type_list.append(pokemon_type['name'])
    print("\nList of pokemon types: " + str(pokemon_type_list))


player_one = retrieve_pokemon_data(pokemon_number)
opponent = retrieve_pokemon_data(opponent_number)

# Player 1 Data
if player_one:
    print("\nPlayer One Pokémon ID: " + str(pokemon_number))
    name_retrieval(player_one)
    height = height_retrieval(player_one)
    weight = weight_retrieval(player_one)
    type_retrieval(player_one)

    # Dictionary for Player 1's Pokémon
    player_dict = {'id': pokemon_number,
                   'name': player_one['name'],
                   'height': height,
                   'weight': weight,
                   'type': player_one['types'][0]['type']['name']
                   }

    print("Player One's Pokémon Dictionary: " + str(player_dict))

else:
    print("Error fetching Player's Pokémon data.\n")

# retrieving opponent's data
if opponent:
    print("\nOpponent Pokémon ID: " + str(opponent_number))
    opponent_name = opponent['name'].title()
    print("Opponent Pokémon Name: " + opponent_name)
    opponent_height = int(opponent['height']) * 10  # Height in cm
    print("Opponent Pokémon Height: " + str(opponent_height) + "cm")
    opponent_weight = int(opponent['weight']) / 10  # Weight in kg
    print("Opponent Pokémon Weight: " + str(opponent_weight) + "kg")
    opponent_type_pokemon = opponent['types'][0]['type']['name'].title()
    print("Opponent Pokémon Type: " + opponent_type_pokemon)

    ## Create dictionary for the opponent's Pokémon
    opponent_dict = {
        'id': opponent_number,
        'name': opponent['name'],
        'height': opponent_height,
        'weight': opponent_weight,
        'type': opponent['types'][0]['type']['name']
    }
    print("Opponent's Pokémon Dictionary:", opponent_dict)
else:
    print("Error fetching Opponent's Pokémon data.\n")


# Battle mode for type
def battle_by_type(player_one_dict, opponent_dict, player_one_wins, opponent_wins):
    type_one = player_one_dict['type']
    type_two = opponent_dict['type']

    type_one_enemy = retrieve_by_type(type_one)

    damage_to_list = []
    for i in type_one_enemy['damage_relations']['double_damage_to']:
        damage_to_list.append(i['name'])

    for i in type_one_enemy['damage_relations']['half_damage_to']:
        damage_to_list.append(i['name'])
    print('\nTypes that damage water type pokemon: ' + str(damage_to_list))
    if type_two in damage_to_list:
        player_one_wins =+ 1
        print("You have WON! ٩>ᴗ<)و")
    else:
        opponent_wins =+ 1
        print("Sorry, you lost (ㅠ﹏ㅠ)")


# Ask the player to choose a stat
print('\n=======================  BATTLE  MODE  =======================')

# Compare the stats of the Player 1 and Opponent
def compare_stat(player_dict, opponent_dict, stat_choice):
    pokemon_stat = player_dict[stat_choice]
    opponent_stat = opponent_dict[stat_choice]


    print(f"Player One's Pokémon {stat_choice}: {pokemon_stat}")
    print(f"Opponent's Pokémon {stat_choice}: {opponent_stat}")

    if pokemon_stat > opponent_stat:
        player_one_wins =+ 1
        return 'You have won this round! ٩>ᴗ<)و'

    elif opponent_stat > pokemon_stat:
        opponent_wins =+ 1
        return 'Sorry, you lost this round (ㅠ﹏ㅠ)'

    else:
        return "It's a draw!"




# Initialize battle for 3 rounds
def start_battle(rounds=3):
    for round_num in range(1, rounds + 1):
        print(f"\n========== ROUND {round_num} ==========")
        stat_choice = input("\nChoose a stat to compare (id, height, weight, type): ").lower()

        pokemon_number = random.randint(1, 151)
        opponent_number = random.randint(1, 151)

        player_one = retrieve_pokemon_data(pokemon_number)
        opponent = retrieve_pokemon_data(opponent_number)

        if player_one and opponent:
            player_dict = {
                'id': pokemon_number,
                'name': player_one['name'],
                'height': player_one['height'],
                'weight': player_one['weight'],
                'type': player_one['types'][0]['type']['name']
            }

            opponent_dict = {
                'id': opponent_number,
                'name': opponent['name'],
                'height': opponent['height'],
                'weight': opponent['weight'],
                'type': opponent['types'][0]['type']['name']
            }

            # Display Pokémon info
            print(f"\nPlayer One's Pokémon: {player_dict['name']}")
            print(f"Opponent's Pokémon: {opponent_dict['name']}")

            if stat_choice == 'type':
                result = battle_by_type(player_dict, opponent_dict, player_one_wins, opponent_wins)
            elif stat_choice in ['id', 'height', 'weight']:
                result = compare_stat(player_dict, opponent_dict, stat_choice)
            else:
                print("Invalid choice, please choose 'id', 'height', 'weight', or 'type'.")
                continue

            print(result)

        else:
            print("Error: One or both Pokémon data couldn't be fetched.\n")

def winning_player(player_one_wins, opponent_wins):
    if player_one_wins > opponent_wins:
        return 'You are the WINNER! ٩>ᴗ<)و'

    elif opponent_wins > player_one_wins:
        return 'Sorry, you are the loser (ㅠ﹏ㅠ)'

    else:
        return "It's a draw!"

start_battle(3)
winning_player(player_one_wins,opponent_wins)
