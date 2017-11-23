class Food:
    def __init__(self, type):
        self.__type = type

class Meat(Food):
    def __init__(self, name):
        Food.__init__(self, 'meat')
        self.__name = name

    def calculate_calories(self):
        pass

class Beef(Meat):
    def __init__(self, weight):
        super().__init__('beef')
        self.__weight = weight

    def calculate_calories(self):
        return self.__weight * 1.5

meal = Beef(200)
print(meal.calculate_calories())
