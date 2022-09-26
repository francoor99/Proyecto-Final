class Enemy:
    def __init__(self, name, age, strength, agi, hp, type):
        self.__name = name
        self.__age = age
        self.__strength = strength
        self.__agi = agi
        self.__hp = hp
        self.__type = type

    def get_name(self):
        return self.__name

    def __str__(self): ## Es para cuando llamo con un print al objeto
        return f'Nombre: {self.__name}\nEdad: {self.__age}\nFuerza: {self.__strength}\nAgilidad: {self.__agi}\nSalud: {self.__hp}\nRaza: {self.__type}'