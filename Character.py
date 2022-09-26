class Character:
    def __init__(self, name, age, strength, agi, hp, type):
        self.__name = name
        self.__age = age
        self.__strength = strength  # 'Fuerza
        self.__agi = agi  # 'Agilidad
        self.__hp = hp  # 'Vida
        self.__type = type

    def edit_name(self, name):
        self.__name = name

    def edit_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def __str__(self): ## Es para cuando llamo con un print al objeto
        return f'Nombre: {self.__name}\nEdad: {self.__age}\nFuerza: {self.__strength}\nAgilidad: {self.__agi}\nSalud: {self.__hp}\nRaza: {self.__type}'


''' vikingo = Character('Wosh', 19, 21, 23, 25, 'Human')
print(vikingo) '''
