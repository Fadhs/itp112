class Person:
    def set_weight(self, weight):
        self.__weight = weight
    def set_height(self, height):
        self.__height = height
    def get_weight(self):
         return self.__weight
    def get_height(self):
        return self.__height
    def get_bmi(self):
        return self.__weight / self.__height ** 2

list = []
for i in range(1, 4):
    height = float(input('Enter height of person' + str(i)))
    weight = float(input('Enter weight of person' + str(i)))
    p = Person()
    p.set_height(height)
    p.set_weight(weight)
    list.append(p)
print('The bmi for the Persons you have entered are: ')
for i in range(3):
    person = list[i]
    print(person.get_bmi())
