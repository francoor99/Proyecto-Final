from Character_Controller import *
from time import sleep


def attack(attack_points):
    attack = 0
    dice1 = randint(1, 6)  # Dado 1
    dice2 = randint(1, 6)  # Dado 2
    lucky = dice1 + dice2
    print("Suma de los dados:", lucky)
    if lucky < 4:
        print('Ataque nulo')
        attack = 0
    elif lucky > 3 and lucky < 7:
        print('Ataque x1')
        attack = attack_points
    elif lucky > 6 and lucky < 9:
        print('Ataque x1.5')
        attack = attack_points * 1.5
    elif lucky == 9 and lucky == 10:
        print('Ataque x2')
        attack = attack_points * 2
    elif lucky == 11:
        print('Ataque x2.5')
        attack = attack_points * 2.5
    elif lucky == 12:
        print('Ataque x3')
        attack = attack_points * 3
    return attack


def reception(attack, agility):
    print("Ataque:", attack, "Agilidad: ", agility)
    if agility == 1:
        return attack
    elif agility == 2:
        return attack - 2
    elif agility == 3 or agility == 4:
        if attack <= 3:
            return 0
        else:
            return attack - 3
    elif agility == 5 or agility == 6:
        if attack <= 4:
            return 0
        else:
            return attack - 4

    elif agility == 7 or agility == 8:
        if attack <= 5:
            return 0
        else:
            return attack - 5
    else:
        if attack <= 7:
            return 0
        else:
            return attack - 7


def combat():
    dead_character = 0
    enemy_counter = 1
    while enemy_counter <11:
        if dead_character == 3:
            print(GAME_OVER_TEXT)
            sleep(3)
            break
        character = select_character()
        while character.get_hp() == 0:
            print(CHOSEN_DEAD_CHARACTER)
            sleep(1)
            character = select_character()
        enemy = dictionary_enemy[enemy_counter]
        print(CHOSEN_CHARACTER, character.get_name())
        print(FIGHT_AGAINST, enemy.get_name())
        character_attack = character.get_strength()
        enemy_attack = enemy.get_strength()
        print(YOUR_CHARACTERS_STRENGTH, character_attack)
        character_life = character.get_hp()
        enemy_life = enemy.get_hp()
        print(YOUR_CHARACTERS_HP, character_life)
        character_agility = character.get_agi()
        enemy_agility = enemy.get_agi()
        print(YOUR_CHARACTERS_AGI, character_agility)
        sleep(5)
        combating = True
        while combating == True:
            if character_life > 0:
                print('<------------------------------------------------>')
                print('Ambos estan vivos')
                damage = reception(attack(character_attack), enemy_agility)
                print('El ataque causa ', damage, ' puntos de daño.')
                enemy_life = enemy_life - damage
                if enemy_life > 0:
                    print('El enemigo quedó con ', enemy_life, ' puntos de vida')
                    print('<------------------------------------------------>')
                    sleep(4)
                    print('El enemigo ataca!!')
                    damage = reception(attack(enemy_attack), character_agility)
                    print('El ataque causa ', damage, ' puntos de daño.')
                    character_life = character_life - damage
                    sleep(4)
                    print('<------------------------------------------------>')
                else:
                    print(COMBAT_WIN_TEXT)
                    sleep(3)
                    combating = False
                    sleep(3)
                    enemy_counter = enemy_counter + 1
                    upgrade_level()
                    add_item(character)
            else:
                print(COMBAT_LOSE_TEXT)
                character._Character__hp = 0
                print(character.get_hp()) #Para ver si anda el hp
                sleep(3)
                dead_character = dead_character + 1
                combating = False
        print()

