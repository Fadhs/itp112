class Account:
    def __init__(self, type, interest_rate):
        self.__type = type
        self.__balance = 0
        self.__interest_rate = interest_rate

    def get_interest(self):
        return (self.__interest_rate + 1)* self.__balance

    # mutator and accessor methods for __balance
