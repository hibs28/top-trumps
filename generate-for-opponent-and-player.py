# Function to generate and display Pokémon for a given role
def generate_pokemon(role):
    pokemon_number = random.randint(1, 151)  # Generate a random number between 1 and 151
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)

    if response.status_code == 200:  # Check if the response is successful
        pokemon = response.json()
        print(f"\n{role}'s Pokémon:")
        name_retrieval(pokemon)
        height_retrieval(pokemon)
        weight_retrieval(pokemon)
        return pokemon  # Return the Pokémon data if needed later
    else:
        print(f"Error: Could not retrieve Pokémon with ID '{pokemon_number}'.")
        return None

# Generate Pokémon for the player
player_pokemon = generate_pokemon("Player")

# Generate Pokémon for the opponent
opponent_pokemon = generate_pokemon("Opponent")
