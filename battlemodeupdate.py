if stat_choice == "height":
        pokemon_stat *= 10
        opponent_stat *= 10
        unit = "cm"
    elif stat_choice == "weight":
        pokemon_stat /= 10
        opponent_stat /= 10
        unit = "kg"
    else:
        unit = ""  # No unit for other stats

    # Display stats with units (if applicable)
    print(f"Player One's Pokémon {stat_choice}: {pokemon_stat}{unit}")
    print(f"Opponent's Pokémon {stat_choice}: {opponent_stat}{unit}")
