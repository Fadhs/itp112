#to let student know they can use the class attribute as the unique number
class Vehicle:
    count = 0

    def __init__(self, initial):
        self.__class__.count +=1
        self.__register_Number = initial + str(self.__class__.count)

    def get_register_number(self):
        return self.__register_Number

    def __str__(self):
        s = "The registration number : " + self.__register_Number
        return s