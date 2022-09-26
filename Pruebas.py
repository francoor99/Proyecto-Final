'''class Character:
    def __init__(self, name, age, strength, agi, con, type):
        self.__name = name
        self.__age = age
        self.__strength = strength
        self.__agi = agi
        self.__con = con
        self.__type = type

    def edit_name(self, name):
        self.__name = name

    def edit_age(self, age):
        self.__age = age

    def get_agi(self):
        return self.__agi

    def __str__(self): ## Es para cuando llamo con un print al objeto
        return f'Nombre: {self.__name}\nEdad: {self.__age}\nFuerza: {self.__strength}\nAgilidad: {self.__agi}\nSalud: {self.__con}\nRaza: {self.__type}'


vikingo = Character('Wosh', 19, 21, 23, 25, 'Human')
print(vikingo.get_agi())
print(vikingo._Character__agi)
vikingo._Character__agi = 2
print(vikingo._Character__agi)'''

'''from random import randint
for i in range(10):
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    print(n1 + n2)'''


'''class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        try:
            return self.elements.pop()
        except IndexError:
            raise ValueError('La pila está vacía')

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def is_empty (self):
        return self.elements == []


pila = Stack()
pila.push(2022)
pila.push(2023)
print(pila.peek())
print(pila.size())
pila.pop()'''


'''class Queue:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        try:
            return self.elements.pop(0)
        except IndexError:
            raise ValueError('La fila está vacía')

    def peek(self):
        return self.elements[0]

    def size(self):
        return len(self.elements)

    def is_empty (self):
        return self.elements == []
fila = Queue()
fila.push(2022)
fila.push(2023)
print(fila.peek())
print(fila.size())
fila.pop()'''
