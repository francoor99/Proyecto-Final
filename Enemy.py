class Enemy:
    def __init__(self, name, level, age, strength, agi, hp):
        self.__name = name
        self.__level = level
        self.__age = age
        self.__strength = strength
        self.__agi = agi
        self.__hp = hp



    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_age(self):
        return self.__age

    def get_strength(self):
        return self.__strength

    def get_agi(self):
        return self.__agi

    def get_hp(self):
        return self.__hp

    def get_type(self):
        return self.__type


    def __str__(self): ## Es para cuando llamo con un print al objeto
        return f'Nombre: {self.__name}\nNivel: {self.level}\nEdad: {self.__age}\nFuerza: {self.__strength}\nAgilidad: {self.__agi}\nSalud: {self.__hp}'

