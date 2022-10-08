from Combat import *
from Constants import *


dictionary_enemy[1] = Enemy("Dark Lord", 1, 150, 4, 5, 4)
dictionary_enemy[2] = Enemy("Anakin Skywalker", 2, 25, 6, 4, 5)
dictionary_enemy[3] = Enemy("Max Steel", 3, 21, 8, 3, 6)
dictionary_enemy[4] = Enemy("Señor Burns", 4, 20, 8, 7, 5)
dictionary_enemy[5] = Enemy("Micah Bell", 5, 5, 9, 4, 10)
dictionary_enemy[6] = Enemy("Darth Vader", 6, 85, 12, 5, 11)
dictionary_enemy[7] = Enemy("Voldemort", 7, 80, 13, 8, 9)
dictionary_enemy[8] = Enemy("El Joker", 8, 35, 10, 15, 10)
dictionary_enemy[9] = Enemy("Davy Jones", 9, 150, 12, 13, 15)
dictionary_enemy[10] = Enemy("Thanos", 10, 6000, 16, 14, 17)

dictionary_characters[1] = Character("Santino", 15, 5, 5, 5, "dwarf")
dictionary_characters[2] = Character("Franco", 20, 5, 5, 5, "human")
dictionary_characters[3] = Character("Dante", 18, 5, 5, 5, "elf")
dead_characters = 0
menu = True
while menu is True:
    constant_menu()
    option = int(input(constant_select_option))
    if option == 1:
        create_character()
    elif option == 2:
        if len(dictionary_characters) == 3:
            combat()
        else:
            print(constant_min_characters)
    elif option == 3:
        delete_character()
    elif option == 4:
        menu = False
    else:
        print(constant_fail)

numero_profe = 2604567238


