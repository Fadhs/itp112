class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__name = ''
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

