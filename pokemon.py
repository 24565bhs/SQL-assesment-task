import sqlite3
DATABASE = 'pokemon.db'
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
def print_all_pokemon():
    try:
        #Find what pokemon the user wants
        pokemon_names = input('What mythical pokemon? ')
        pokemon_names = pokemon_names.title()
        cursor.execute("SELECT * FROM pokemon WHERE pokemon_name = ?;", (pokemon_names,))
        results = cursor.fetchone()
        #print info about the pokemon
        print(f'Pokedex: {results[0]}')
        print(f'Pokemon_name: {results[1]}')
        print(f'Pokemon_type: {results[2]}')

        return
    except TypeError:
        #Pokemon does not exist
        print('That is not a valid pokemon.')
        

while True:
    try:
        #find out what user wants
        print('===========================================================================================================================================')
        print('Welcome to the mythical pokemon program.')
        print("Type the name of a pokemon and find out it's type, pokedex number, strengths and weaknesses.")
        print('===========================================================================================================================================')
        print('Click 1 to enter a pokemon.')
        print("Click 2 to find good match ups for your pokemon")
        print('Click 3 to end program.')
        option = int(input('Choose which option you want: '))
        if option == 1:
            #Find information on a pokemon
            print('===========================================================================================================================================')
            print('<Enter the name of any Mythical pokemon>')
            print_all_pokemon()
        elif option == 2:
            print('===========================================================================================================================================')
            pokemon_in_use = input('What pokemon are you using? ')
            pokemon_in_use = pokemon_in_use.title()
            cursor.execute("SELECT pokemon_name, pokemon_type, pokemon_weakness, pokemon_strength FROM pokemon WHERE pokemon_name = ?;", (pokemon_in_use,))
            results = cursor.fetchone()
            print(f'You are using {results[0]}.')
            print(f'{results[0]} is a {results[1]} type.')
            print(f'Do not match {results[0]} against {results[2]} pokemon.')
            print(f'Only use {results[0]} against {results[3]} pokemon.')
        elif option == 3:
            #ending program
            print('===========================================================================================================================================')
            print('Goodbye')
            break
    except ValueError:
        print("Please enter a valid number, not text.")