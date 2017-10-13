class Person:

    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    def get_bmi(self):
        return self.__weight / self.__height ** 2

p = Person(71, 1.76)
print(p.get_bmi())

