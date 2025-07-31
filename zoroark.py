# Pokémon Adventure: The Search for Zoroark
# A simple Python program using basic concepts

def main():
    print("Welcome to the Pokémon World!\n")
    
    # List of Pokémon
    pokemon_list = [
        "Pikachu", "Charizard", "Bulbasaur", "Squirtle", 
        "Jigglypuff", "Gengar", "Eevee", "Snorlax",
        "Mewtwo", "Lucario", "Zoroark", "Greninja"
    ]
    
    # Pokémon type dictionary
    pokemon_types = {
        "Pikachu": "Electric",
        "Charizard": "Fire/Flying",
        "Bulbasaur": "Grass/Poison",
        "Squirtle": "Water",
        "Jigglypuff": "Normal/Fairy",
        "Gengar": "Ghost/Poison",
        "Eevee": "Normal",
        "Snorlax": "Normal",
        "Mewtwo": "Psychic",
        "Lucario": "Fighting/Steel",
        "Zoroark": "Dark",
        "Greninja": "Water/Dark"
    }
    
    # Pokémon HP stats
    pokemon_hp = {
        "Pikachu": 35,
        "Charizard": 78,
        "Bulbasaur": 45,
        "Squirtle": 44,
        "Jigglypuff": 115,
        "Gengar": 60,
        "Eevee": 55,
        "Snorlax": 160,
        "Mewtwo": 106,
        "Lucario": 70,
        "Zoroark": 60,
        "Greninja": 72
    }
    
    # Introduction
    print("Our story begins in a forest where rumors say")
    print("the elusive Zoroark has been sighted!\n")
    
    # Player setup
    player_name = input("What's your name, Trainer? ")
    print(f"\nGood luck, {player_name}! Let's find Zoroark!\n")
    
    # Game variables
    found_zoroark = False
    attempts = 0
    max_attempts = 5
    inventory = []
    
    # Game loop
    while not found_zoroark and attempts < max_attempts:
        print("\nWhat will you do?")
        print("1. Search the forest")
        print("2. Check your Pokédex")
        print("3. Rest at the camp")
        print("4. Quit the search")
        
        choice = input("Choose (1-4): ")
        
        if choice == "1":
            attempts += 1
            found_pokemon = search_forest(pokemon_list)
            
            if found_pokemon == "Zoroark":
                found_zoroark = True
                print("\nA wild Zoroark appeared!")
                print("It's using its illusion powers!")
                zoroark_battle(pokemon_types, pokemon_hp)
            else:
                print(f"\nYou found a {found_pokemon}!")
                if found_pokemon not in inventory:
                    inventory.append(found_pokemon)
                
        elif choice == "2":
            check_pokedex(inventory, pokemon_types)
            
        elif choice == "3":
            print("\nYou rest at camp and regain your strength.")
            print(f"Attempts remaining: {max_attempts - attempts}")
            
        elif choice == "4":
            print("\nYou gave up the search...")
            break
            
        else:
            print("\nInvalid choice! Try again.")
    
    # Game end
    if found_zoroark:
        print("\nCongratulations! You found Zoroark!")
        print("You completed your mission!")
    else:
        print("\nZoroark remains elusive...")
        print("Better luck next time!")
    
    print("\nPokémon encountered:")
    for pokemon in inventory:
        print(f"- {pokemon}")

def search_forest(pokemon_list):
    """Randomly find a Pokémon in the forest"""
    import random
    # Zoroark has a 10% chance to appear
    if random.randint(1, 10) == 1:
        return "Zoroark"
    else:
        return random.choice([p for p in pokemon_list if p != "Zoroark"])

def zoroark_battle(pokemon_types, pokemon_hp):
    """Special battle sequence with Zoroark"""
    print("\nZoroark is trying to trick you!")
    
    # Zoroark's illusion
    fake_pokemon = "Pikachu"
    print(f"It disguises itself as {fake_pokemon}!")
    
    # Player's choice
    print("\nWhat will you do?")
    print("1. Attack with a Water move")
    print("2. Use a Poké Ball")
    print("3. Try to see through the illusion")
    
    choice = input("Choose (1-3): ")
    
    if choice == "3":
        print("\nYou look closely and notice something odd...")
        print("The illusion fades! It's Zoroark!")
        print("Zoroark is impressed by your observation!")
    else:
        print(f"\nYour attack passes through the {fake_pokemon}!")
        print("It was an illusion all along!")
        print("Zoroark reveals itself and escapes laughing!")

def check_pokedex(inventory, pokemon_types):
    """Display caught Pokémon info"""
    if not inventory:
        print("\nYour Pokédex is empty! Go find some Pokémon!")
    else:
        print("\nYour Pokédex:")
        for pokemon in inventory:
            print(f"{pokemon} - Type: {pokemon_types.get(pokemon, 'Unknown')}")

if __name__ == "__main__":
    main()