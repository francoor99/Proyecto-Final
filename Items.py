class Items:
    def __init__(self, name, strength, agi, hp):
        self.__name = name
        self.__strength = strength  # 'Fuerza
        self.__agi = agi  # 'Agilidad
        self.__hp = hp  # 'Vida

    def get_name(self):
        return self.__name

    def get_strength(self):
        return self.__strength

    def get_agi(self):
        return self.__agi

    def get_hp(self):
        return self.__hp



item1 = Items("Sable de luz de Luke", 3, 2, 0)
item2 = Items("Mjolnir", 2, 0, 0)
item3 = Items("StormBreaker", 4, 2, 0)
item4 = Items("Mark 3", 2, 1, 4)
item5 = Items("Elixir basico", 0, 0, 5)
item6 = Items("Anillo Unico", 0, 1, 4)
item7 = Items("Botas de Hermes", 0, 1, 4)
item8 = Items("Espadas del Caos", 4, 1, 0)
item9 = Items("MP44", 5, 0, 0)
item10 = Items("Escudo del Cap", 0, 2, 4)
item11 = Items("Suero del supersoldado", 0, 2, 5)
items_list = [item1, item2, item3, item4, item5, item6, item7, item8,item9, item10, item11]




