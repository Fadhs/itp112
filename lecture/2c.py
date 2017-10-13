class Person:

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def get_bmi(self):
        return self.__weight / self.__height ** 2

p = Person()
print(p.get_height())
p.set_height(1.76)
p.set_weight(71)
print(p.get_bmi())

