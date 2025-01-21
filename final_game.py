import random
import requests

# generate a random number between 1 and 151
pokemon_number = random.randint(1, 151)
opponent_number = random.randint(1, 151)

# ASCII for Pokémon logo => the reason we use triple speech marks is for strings that span multiple lines
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
# Does a GET call for the API, and returns the json response if 200 else print error message and return nothing
# Returns response.json
def retrieve_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()

    else:
        print(f"Error: Could not find Pokémon with this ID '{pokemon_number}'. Please check the number.")
        return None


# Function to call types for Pokémon
# Does a GET call to retrieve a list of Pokémon types or if with a path variable gets details of that specific type
# Returns response.json
def retrieve_by_type(pokemon_type):
    pokemon_type_url = 'https://pokeapi.co/api/v2/type/{}'.format(pokemon_type)
    return requests.get(pokemon_type_url).json()


# Retrieves weight from API GET retrieve_pokemon_data response and converts it from hectograms to kilograms.
# Returns Print
def weight_retrieval(pokemon, player):
    weight = pokemon['weight']
    weight = int(weight) / 10
    return print(player + " Pokémon Weight: " + str(weight) + " kg")


# Retrieves name of Pokémon from API retrieve_pokemon_data response json and formats it.
# Returns Print
def name_retrieval(pokemon, player):
    name = pokemon['name'].title()
    return print(player + " Pokémon Name: " + name)


# Retrieves height from the API Get retrieve_pokemon_data response converts it from decimeters to centimetres
# Returns Print
def height_retrieval(pokemon, player):
    height = pokemon['height']
    height = int(height) * 10
    return print(player + " Pokémon Height: " + str(height) + " cm")


# Retrieves type from API Get retrieve_pokemon_data response
# Returns Print
def type_retrieval(pokemon, player):
    type_pokemon = pokemon['types'][0]['type']['name'].title()
    return print(player + " Pokémon Type: " + type_pokemon)


# Gets a List of Pokémon types from API GET retrieve_by_type with empty path variable
# Returns Print
def get_pokemon_type_list():
    pokemon_response = retrieve_by_type("")
    pokemon_type_list = []
    for pokemon_type in pokemon_response['results']:
        pokemon_type_list.append(pokemon_type['name'])
    print("\nList of pokemon types: " + str(pokemon_type_list))


# Create a variable for the json both player and opponent
player_one = retrieve_pokemon_data(pokemon_number)
opponent = retrieve_pokemon_data(opponent_number)


# Function to create the dictionaries using the two jsons, Returns two dictionaries
def define_dict_player_and_opponent(player_one, opponent):
    player_dict = None  # Initialise player_dict
    opponent_dict = None  # Initialise opponent_dict

    # IF statement to check which json we are using and set it to correct corresponding dictionary ELSE Error message
    # Player 1 Data
    if player_one:
        # Create a dictionary for Player 1's Pokémon
        player_dict = {'id': pokemon_number,
                       'name': player_one['name'],
                       'height': player_one['height'],
                       'weight': player_one['weight'],
                       'type': player_one['types'][0]['type']['name']
                       }
    else:
        print("Error fetching Player's Pokémon data.\n")

    # Opponent's data
    if opponent:
        # Create a dictionary for the opponent's Pokémon
        opponent_dict = {
            'id': opponent_number,
            'name': opponent['name'],
            'height': opponent['height'],
            'weight': opponent['weight'],
            'type': opponent['types'][0]['type']['name']
        }
    else:
        print("Error fetching Opponent's Pokémon data.\n")

    return player_dict, opponent_dict


# Battle Mode for Type, Returns String
def battle_by_type(player_one_dict, opponent_dict, player_one_wins, opponent_wins):
    # Takes the type from dictionaries and set as a variable
    type_one = player_one_dict['type']
    type_two = opponent_dict['type']

    # Gets a response for Player One's Pokémon type
    type_one_enemy = retrieve_by_type(type_one)

    # Initialise the list
    damage_to_list = []
    # In the response they have multiple enemies, we filter the one the player can damage to
    # Loops through list and add it in.
    for i in type_one_enemy['damage_relations']['double_damage_to']:
        damage_to_list.append(i['name'])

    for i in type_one_enemy['damage_relations']['half_damage_to']:
        damage_to_list.append(i['name'])
    # Print the list of Pokémon types that damages Player Pokémon type
    print('Types that damage ' + type_one + ' type pokemon: ' + str(damage_to_list))

    # Prints both player's Pokémon type formating the type.
    print(f"\nPlayer One's Pokémon Type: {type_one.title()}")
    print(f"Opponent's Pokémon Type: {type_two.title()}")

    # Compares opponent's Pokémon type is within the list
    # IF opponent's type is in list then output win and add 1 to opponent's win
    # ELSE output loss and add 1 to opponent's win
    if type_two in damage_to_list:
        player_one_wins += 1
        return "You have WON! ٩>ᴗ<)و", player_one_wins, opponent_wins
    else:
        opponent_wins += 1
        return "Sorry, you lost (ㅠ﹏ㅠ)", player_one_wins, opponent_wins


# Ask the player to choose a stat
print('\n=======================  BATTLE  MODE  =======================')


# Compare the stats of the Player 1 and Opponent
# Returns a string
def compare_stat(player_dict, opponent_dict, stat_choice, player_one_wins, opponent_wins):
    # Get the stat values of each player e.g. if stat_choice = "height" it'll be player_dict['height']
    player_stat = player_dict[stat_choice]
    opponent_stat = opponent_dict[stat_choice]

    # Checks what player stat they have chosen and format it
    if stat_choice == "weight":
        player_stat_display = f"{player_stat / 10} kg"  # Convert from hectograms to kilograms
        opponent_stat_display = f"{opponent_stat / 10} kg"  # Convert from hectograms to kilograms
    elif stat_choice == "height":
        player_stat_display = f"{player_stat * 10} cm"  # Convert from meters to centimeters
        opponent_stat_display = f"{opponent_stat * 10} cm"  # Convert from meters to centimeters
    else:
        player_stat_display = player_stat
        opponent_stat_display = opponent_stat

    print(f"Player One's Pokémon {stat_choice.title()}: {player_stat_display}")
    print(f"Opponent's Pokémon {stat_choice.title()}: {opponent_stat_display}")

    # Comparison (same logic for ID, Height and Weight)
    if player_stat > opponent_stat:
        player_one_wins += 1
        return 'You have won this round! ٩>ᴗ<)و', player_one_wins, opponent_wins

    elif opponent_stat > player_stat:
        opponent_wins += 1
        return 'Sorry, you lost this round (ㅠ﹏ㅠ)', player_one_wins, opponent_wins

    else:
        return "It's a draw!", player_one_wins, opponent_wins


# Logic for checking which player has won the most games
def winning_player(player_one_wins, opponent_wins):
    if player_one_wins > opponent_wins:
        return '    ⋆｡°✩ You are the WINNER! ٩>ᴗ<)و ✩°｡⋆'
    elif opponent_wins > player_one_wins:
        return ' ・.˚ Sorry, you are the loser (ㅠ﹏ㅠ) ˚.・'
    else:
        return "              It's a draw!"


# Initialize battle for 3 rounds
# Does the logic for each round
def start_battle(rounds=3):
    player_one_wins = 0
    opponent_wins = 0
    for round_num in range(1, rounds + 1):
        # Generates a new Pokémon each round for both players
        pokemon_number = random.randint(1, 151)
        opponent_number = random.randint(1, 151)

        player_one = retrieve_pokemon_data(pokemon_number)
        opponent = retrieve_pokemon_data(opponent_number)

        player_dict, opponent_dict = define_dict_player_and_opponent(player_one, opponent)

        # Display Pokémon info
        print(f"\n========================   ROUND {round_num}   ========================")

        print("Player One's Pokémon ID: " + str(pokemon_number))
        name_retrieval(player_one, "Player One")
        height_retrieval(player_one, "Player One")
        weight_retrieval(player_one, "Player One")
        type_retrieval(player_one, "Player One")

        # gets stat_choice from user as an input - currently it's not case-sensitive
        stat_choice = input("\nChoose a stat to compare (id, height, weight, type): ").lower()

        print(f"\nPlayer One's Pokémon: {player_dict['name'].title()}")
        print(" ------------------- VS ------------------- ")
        print(f"Opponent's Pokémon: {opponent_dict['name'].title()}\n")

        # Checks if the user inputs the correct options if not then
        if stat_choice == 'type':
            result, player_one_wins, opponent_wins = battle_by_type(player_dict, opponent_dict, player_one_wins,
                                                                    opponent_wins)
        elif stat_choice in ['id', 'height', 'weight']:
            result, player_one_wins, opponent_wins = compare_stat(player_dict, opponent_dict, stat_choice,
                                                                  player_one_wins, opponent_wins)
        else:
            print("Invalid choice, please choose 'id', 'height', 'weight', or 'type'.")
            continue  # If user enters the wrong options it continues with the loop

        # prints results
        print("\n" + result)

        # Prints at the end of the round the opponent's details
        print("\nOpponents Stats")
        print("-" * 18)
        print("Opponent Pokémon ID: " + str(opponent_number))
        name_retrieval(opponent, "Opponent")
        height_retrieval(opponent, "Opponent")
        weight_retrieval(opponent, "Opponent")
        type_retrieval(opponent, "Opponent")


    # Print winner
    print('')
    print('╔' + '═' * 41 + '╗')  # '═'*41 -> print the string 41 times next to each other
    print(f"{winning_player(player_one_wins, opponent_wins)}")
    print('╚' + '═' * 41 + '╝')

start_battle(3)
