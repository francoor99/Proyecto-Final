from Character_Controller import *
from random import randint
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
        print('Ataque x2')
        attack = attack_points * 2
    elif lucky == 9 and lucky == 10:
        print('Ataque x3')
        attack = attack_points * 3
    elif lucky == 11:
        print('Ataque x4')
        attack = attack_points * 4
    elif lucky == 12:
        print('Ataque x5')
        attack = attack_points * 5
    return attack


def reception(attack, agility):
    print("Ataque:", attack, "Agilidad: ", agility)
    if agility == 1:
        return attack
    elif agility == 2:
        return attack - 2
    elif agility == 3 or agility == 4:
        return attack - 3
    elif agility == 5 or agility == 6:
        return attack - 4
    elif agility == 7 or agility == 8:
        return attack - 5
    else:
        return attack - 7


def combat(character):
    for i in range(10):
        enemy = dictionary_enemy[i+1]  # 'FALTA QUE ELIJA UNO ALEATORIO
        print('Su personaje es: ', character.get_name())
        print('Va a pelear contra: ', enemy.get_name())
        character_attack = character.get_strength()
        enemy_attack = enemy.get_strength()
        print('La fuerza de tu personaje es: ', character_attack)
        character_life = character.get_hp()
        enemy_life = enemy.get_hp()
        print('La vida de tu personaje es: ', character_life)
        character_agility = character.get_agi()
        enemy_agility = enemy.get_agi()
        print('La agilidad de tu personaje es: ', character_agility)
        sleep(5)
        combating = True
        character_death = False
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
                    sleep(5)
                    print('El enemigo ataca!!')
                    damage = reception(attack(enemy_attack), character_agility)
                    print('El ataque causa ', damage, ' puntos de daño.')
                    character_life = character_life + damage
                    print('<------------------------------------------------>')
                else:
                    print('El enemigo ha muerto, has ganado este combate.')
                    sleep(3)
                    combating = False
                    sleep(3)
            else:
                print('Has muerto, el enemigo ganó el combate. :(')
                character._Character__hp = 0
                print(character.get_hp())
                sleep(3)
                combating = False
                character_death = True
        if character_death == True:
            break
