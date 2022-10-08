from Constants import *
from Enemy import *
from Character import *

dictionary_characters = {}
id_object = 0
dictionary_enemy = {}
id_enemy = 0

def create_character():
    global id_object
    id_object += 1
    name = str(input(constant_name))
    age = int(input(constant_age))
    validation = False
    while validation is False:
        print('La suma entre los tres atributos (Fuerza - Agilidad - Vida tienen que sumar 15)')
        strength = int(input('Ingrese la furza del personaje (mínimo 1): '))
        agi = int(input('Ingrese la agilidad del personaje (mínimo 1): '))
        hp = int(input('Ingrese la vida: '))
        if strength + agi + hp == 15 and strength >= 1 and agi >= 1 and hp >= 1:
            validation = True
        else:
            print(constant_fail)
    validation = False
    while validation == False:
        constant_raza()
        option = int(input('Ingrese el número: '))
        if option == 1:
            type = 'human'
            strength += 2
            validation = True
        elif option == 2:
            type = 'elf'
            agi += 2
            validation = True
        elif option == 3:
            type = 'dwarf'
            hp += 2
            validation = True
        else:
            print(constant_fail)
    object = id_object
    object = Character(name, age, strength, agi, hp, type)
    dictionary_characters[id_object] = object
    print(object)


'''def create_enemy():
    print(constant_enemy)
    global id_enemy
    id_enemy += 1
    name = str(input(constant_name))
    age = int(input(constant_age))
    validation = False
    while validation is False:
        print('La suma entre los tres atributos (Fuerza - Agilidad - Vida tienen que sumar 10)')
        strength = int(input('Ingrese la furza del enemigo (mínimo 1): '))
        agi = int(input('Ingrese la agilidad del enemigo (mínimo 1): '))
        hp = int(input('Ingrese la vida: '))
        if strength + agi + hp == 10 and strength >= 1 and agi >= 1 and hp >= 1:
            validation = True
        else:
            print(constant_fail)
    validation = False
    while validation == False:
        constant_raza()
        option = int(input('Ingrese el número: '))
        if option == 1:
            type = 'human'
            strength += 2
            validation = True
        elif option == 2:
            type = 'elf'
            agi += 2
            validation = True
        elif option == 3:
            type = 'dwarf'
            hp += 2
            validation = True
        else:
            print(constant_fail)
    object = id_enemy
    object = Enemy(name, age, strength, agi, hp)
    dictionary_enemy[id_object] = object
    print(constant_created_character)
    print(object)'''


"""def select_character():
    chosen_character = None
    while chosen_character.get_hp() == 0 or None:
        print(constant_select_character)
        values = dictionary_characters.values()
        nro = 1
        for i in values:
            print(nro, ' - ', i.get_name())
            nro += 1
        character_option = int(input(constant_character_option))
        chosen_character = dictionary_characters[character_option]
        if chosen_character.get_hp() == 0:
            print("El personaje elegido esta muerto, elija otro ")
        return chosen_character"""



def select_character():
    print(constant_select_character)
    values = dictionary_characters.values()
    nro = 1
    for i in values:
        print(nro, ' - ', i.get_name())
        nro += 1
    character_option = int(input(constant_character_option))
    chosen_character = dictionary_characters[character_option]
    while character_option is not 1 or 2 or 3:
        print("Eligio una opcion no valida, ingrese un personaje:")
        character_option = int(input(constant_character_option))
        chosen_character = dictionary_characters[character_option]
    return chosen_character






def delete_character():
    print(constant_delete_character)






