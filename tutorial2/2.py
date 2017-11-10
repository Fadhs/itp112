class BankAccount:
    def __init__(self):
        self.__balance = 0
    def get_balance(self):
        return self.__balance
    def withdraw(self, amount):
        if self.__balance < amount:
            print('Your balance', self.__balance, 'is not enough')
        else:
            self.__balance -= amount
    def deposit(self, amount):
        self.__balance += amount

account = BankAccount()
account.deposit(5000)
account.withdraw(4500)
print('Account balance is', account.get_balance())
