from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    @abstractmethod
    def produce_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, number_of_legs):
        Animal.__init__(self, name, age)
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

    def __str__(self):
        return f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'

class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient):
        Animal.__init__(self, name, age)
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

    def __str__(self):
        return f'Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}'

class Snake(Animal):
    def __init__(self, name, age, cruelty_coefficient ):
        Animal.__init__(self, name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

    def __str__(self):
        return f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'

My_list = []

while True:
    string = input()
    if string == "I'm your Huckleberry":
        break

    string2 = string.split()

    if string2[0] == 'Dog':
        a = Dog(string2[1], int(string2[2]), int(string2[3]))
        My_list.append(a)
    if string2[0] == 'Cat':
        b = Cat(string2[1], int(string2[2]), int(string2[3]))
        My_list.append(b)
    if string2[0] == 'Snake':
        c = Snake(string2[1], int(string2[2]), int(string2[3]))
        My_list.append(c)
    if string2[0] == 'talk':
        name = string2[1]
        name_obj = list(filter(lambda animal: animal.name == name, My_list))[0]
        print(name_obj.produce_sound())


dogs = list(filter(lambda animal: isinstance(animal, Dog), My_list))
cats = list(filter(lambda animal: isinstance(animal, Cat), My_list))
snakes = list(filter(lambda animal: isinstance(animal, Snake), My_list))
sorted_animals = dogs + cats + snakes

for n in sorted_animals:
    print(n)








