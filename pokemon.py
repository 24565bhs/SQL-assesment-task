import sqlite3
DATABASE = 'pokemon.db'
def print_all_pokemon():
    try:
        pokemon_names = input('What mythical pokemon? ')
        pokemon_names = pokemon_names.title()
        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM pokemon WHERE pokemon_name = ?;", (pokemon_names,))
            results = cursor.fetchone()
            print(f'Pokedex: {results[0]}')
            print(f'Pokemon_name: {results[1]}')
            print(f'Pokemon_type: {results[2]}')
            print(f'Pokemon_strength: {results[3]}')
            print(f'Pokemon_weakness: {results[4]}')
            return
    except TypeError:
        print('That is not a valid pokemon.')
        

while True:
    try:
        print('===========================================================================================================================================')
        print('Welcome to the mythical pokemon program.')
        print("Type the name of a pokemon and find out it's type, pokedex number, strengths and weaknesses.")
        print('===========================================================================================================================================')
        print('Click 1 to enter a pokemon.')
        print('Click 2 to end program.')
        option = input('Choose which option you want: ')
        if option == 1:
            print('===========================================================================================================================================')
            print('<Enter the name of any Mythical pokemon>')
            print_all_pokemon()
        elif option == 2:
            print('===========================================================================================================================================')
            print('Goodbye')
            break
    except ValueError:
        print("Please enter a valid number, not text.🤪🤪🤪")