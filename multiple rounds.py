#execute multiple rounds 
def start_battle(round=3):
  for round_num in range(1, rounds + 1):
    print(f"\n=========== ROUND{round_num}=========== ")

    pokemon_number = random.randint(a:1, b:151)
    opponent_number = random.randint(a:1, b:151)

    player_one = retrieve_pokemon(pokemon_number)
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
  
     # Display each Pokémon's info
            print(f"\nPlayer One's Pokémon: {player_dict['name']}")
            print(f"Opponent's Pokémon: {opponent_dict['name']}")

            # Ask the player to choose a stat
            stat_choice = input("\nChoose a stat to compare (height, weight, type): ").lower()

            if stat_choice == 'type':
                result = battle_by_type(player_dict, opponent_dict)
            elif stat_choice in ['height', 'weight']:
                result = compare_stat(player_dict, opponent_dict, stat_choice)
            else:
                print("Invalid choice, please choose 'height', 'weight', or 'type'.")
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

