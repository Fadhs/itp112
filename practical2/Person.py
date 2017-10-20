class Person:
    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__phone = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

me = Person()
me.set_name('Lee')
me.set_address('AMK')
me.set_phone(12345678)
