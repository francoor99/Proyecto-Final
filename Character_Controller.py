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
        strength = int(input(STRENGTH_INPUT))
        agi = int(input(AGILITY_INPUT))
        hp = int(input(HP_INPUT))
        if strength + agi + hp == 15 and strength >= 1 and agi >= 1 and hp >= 1:
            validation = True
        else:
            print(FAIL_TEXT)
    validation = False
    while validation == False:
        print(RAZA_TEXT)
        option = str(input(TYPE_INPUT))
        option.lower()
        if option == "humano":
            type = 'human'
            strength += 2
            validation = True
        elif option == "elfo":
            type = 'elf'
            agi += 2
            validation = True
        elif option == "enano":
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
        if i.get_hp() == 0:
            print(nro, LINE, i.get_name(), DEAD_ICON)
            nro += 1
        else:
            print(nro, LINE, i.get_name())
            nro += 1
    character_option = int(input(CHARACTER_OPTION_TEXT))
    if character_option == 120731:
        print(IM_IRON_MAN)
        return Character("Iron Man", 53, 100, 100, 100, BEST_SUPER_HERO)
    chosen_character = dictionary_characters[character_option]
    while 0 << character_option << 4 :
        print(INCORRECT_OPTION)
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
                print(f' {CHARACTER_TEXT} {dictionary_characters[i].get_name()} {LEVEL_UP_F_TEXT}')
            elif stat == 2:
                agi = dictionary_characters[i].get_agi() + 1
                dictionary_characters[i].set_agi(agi)
                print(f' {CHARACTER_TEXT} {dictionary_characters[i].get_name()} {LEVEL_UP_A_TEXT}')
            elif stat == 3:
                hp = dictionary_characters[i].get_hp() + 1
                dictionary_characters[i].set_hp(hp)
                print(f' {CHARACTER_TEXT} {dictionary_characters[i].get_name()} {LEVEL_UP_HP_TEXT}')

def add_item(character):
    i = randint(0, 15)
    if 0 <= i <= 10:
        item = items_list[i]
        print(f'{ENEMY_DROP_TEXT} {item.get_name()}')
        time.sleep(2)
        strength = character.get_strength() + item.get_strength()
        character.set_strength(strength)
        print(f' {CHARACTER_TEXT} {character.get_name()} {RAISED_TEXT} {item.get_strength()} {FORCE_TEXT}')
        agi = character.get_agi() + item.get_agi()
        character.set_agi(agi)
        print(f' {CHARACTER_TEXT} {character.get_name()} {RAISED_TEXT} {item.get_agi()} {AGILITY_TEXT_2}')
        hp = character.get_hp() + item.get_hp()
        character.set_hp(hp)
        print(f' {CHARACTER_TEXT} {character.get_name()} {RAISED_TEXT} {item.get_hp()} {HP_TEXT}')
        time.sleep(2)


def delete_character():
    print(DELETE_CHARACTER_TEXT)






