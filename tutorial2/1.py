class Person:
    def __init__(self):
        self.__first_name = ''
        self.__last_name = ''

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_full_name(self):
        if self.__first_name == '' or self.__last_name == '':
            return 'Unknown'
        else:
            return self.__first_name + ' ' + self.__last_name

p = Person()
p.set_first_name('John')
p.set_last_name('Lee')
print(p.get_full_name())
