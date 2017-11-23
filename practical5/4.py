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

class Bar:
    beverages = []
    orders = []
    def __init__(self):
        self.create_beverages()

    def create_beverages(self):
        m1 = Mocktail('Lemonade Punch', 5.9)
        self.add_beverage(m1)
        m2 = Mocktail('Tomato Lassi', 6.9)
        self.add_beverage(m2)
        c1 = Cocktail('Bloody Mary', 10.9, 20)
        self.add_beverage(c1)
        c2 = Cocktail('Singapore Sling', 11.9, 30)
        self.add_beverage(c2)

    def add_beverage(self, beverage):
        self.__class__.beverages.append(beverage)

    def show_menu(self):
        while True:
            number = 1
            for beverage in self.__class__.beverages:
                print(number, beverage)
                number += 1
            print('0 Quit Program')
            order = int(input('Enter your choice (0,1,2,3,4): '))
            if order == 0:
                break
            else:
                beverage = self.__class__.beverages[order-1]
                self.__class__.orders.append(beverage)


    def display_orders(self):
        print('The orders are:')
        total = 0
        for order in self.__class__.orders:
            print(order)
            total += order.get_price()
        print('The total amount is', total)



bar = Bar()
bar.show_menu()
bar.display_orders()
