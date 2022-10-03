from Combat import *
from Constants import *


menu = True
while menu is True:
    constant_menu()
    option = int(input(constant_select_option))
    if option == 1:
        create_character()
    elif option == 2:
        create_enemy()
    elif option == 3:
        select_character()
        character_option = int(input(constant_character_option))
        print(dictionary_characters[character_option])
    elif option == 4:
        select_character()
        character_option = int(input(constant_character_option))
        print(dictionary_characters[character_option])
        combat(dictionary_characters[character_option])
    elif option == 5:
        delete_character()
    elif option == 6:
        menu = False
    else:
        print(constant_fail)

numero_profe = 2604567238
franco = 'franco'