class Beverage:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price

class Mocktail(Beverage):
    def __init__(self, name, price):
        super().__init__(name, price)
    def __str__(self):
        return '{} at {}'.format(self.get_name(), self.get_price())

class Cocktail(Beverage):
    def __init__(self, name, price, alcohol):
        super().__init__(name, price)
        self.__alcohol = alcohol
    def get_alcohol(self):
        return self.__alcohol
    def __str__(self):
        return '{} with {}% of alcohol at {}'.format(self.get_name(), self.__alcohol, self.get_price())
