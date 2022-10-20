from Constants import *
from Enemy import *
from Character import *
from Items import *
from random import randint
import time


dictionary_characters = {}
id_object = 0
dictionary_enemy = {}
id_enemy = 0

def create_character():
    global id_object
    id_object += 1
    name = str(input(NAME_INPUT_TEXT))
    age = int(input(AGE_INPUT_TEXT))
    validation = False
    while validation is False:
        print(MAX_STATS_TEXT)
        strength = int(input('Ingrese la furza del personaje (mínimo 1): '))
        agi = int(input('Ingrese la agilidad del personaje (mínimo 1): '))
        hp = int(input('Ingrese la vida: '))
        if strength + agi + hp == 15 and strength >= 1 and agi >= 1 and hp >= 1:
            validation = True
        else:
            print(FAIL_TEXT)
    validation = False
    while validation == False:
        """constant_raza()"""
        print(RAZA_TEXT)
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
            print(FAIL_TEXT)
    object = id_object
    object = Character(name, age, strength, agi, hp, type)
    dictionary_characters[id_object] = object
    print(object)


def select_character():
    print(SELECT_CHARACTER_TEXT)
    values = dictionary_characters.values()
    nro = 1
    for i in values:
        print(nro, ' - ', i.get_name())
        nro += 1
    character_option = int(input(CHARACTER_OPTION_TEXT))
    if character_option == 120731:
        print("Yo soy Iron Man")
        return Character("Iron Man", 53, 100, 100, 100, "Mejor superheroe de la historia")
    chosen_character = dictionary_characters[character_option]
    while 0 << character_option << 4 :
        print("Eligio una opcion no valida, ingrese un personaje:")
        character_option = int(input(CHARACTER_OPTION_TEXT))
        chosen_character = dictionary_characters[character_option]
    return chosen_character


def upgrade_level():
    for i in dictionary_characters:
        if dictionary_characters[i].get_hp() != 0:
            level = dictionary_characters[i].get_level() + 1
            dictionary_characters[i].set_level(level)
            stat = randint(1, 3)
            if stat == 1:
                strength = dictionary_characters[i].get_strength() + 1
                dictionary_characters[i].set_strength(strength)
                print(f'El personaje {dictionary_characters[i].get_name()} aumento 1 de fuerza')
            elif stat == 2:
                agi = dictionary_characters[i].get_agi() + 1
                dictionary_characters[i].set_agi(agi)
                print(f'El personaje {dictionary_characters[i].get_name()} aumento 1 de agilidad')
            elif stat == 3:
                hp = dictionary_characters[i].get_hp() + 1
                dictionary_characters[i].set_hp(hp)
                print(f'El personaje {dictionary_characters[i].get_name()} aumento 1 de hp')

def add_item(character):
    i = randint(0, 15)
    if 0 <= i <= 10:
        item = items_list[i]
        print(f'El enemigo droppeo {item.get_name()}')
        strength = character.get_strength() + item.get_strength()
        character.set_strength(strength)
        print(f'El personaje {character.get_name()} aumento {item.get_strength()} de fuerza')
        agi = character.get_agi() + item.get_agi()
        character.set_agi(agi)
        print(f'El personaje {character.get_name()} aumento {item.get_agi()} de agilidad')
        hp = character.get_hp() + item.get_hp()
        character.set_hp(hp)
        print(f'El personaje {character.get_name()} aumento {item.get_hp()} de hp')
        time.sleep(2)


def delete_character():
    print(DELETE_CHARACTER_TEXT)






