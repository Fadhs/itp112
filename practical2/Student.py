class Student:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        self.__mark = 0.0

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_mark(self):
        return self.__mark

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_mark(self, mark):
        self.__mark = mark

    def __str__(self):
        s ='Name : {}, Gendoer : {} and Marks : {}'.format(self.get_name(), self.get_gender(), self.get_mark())
        return s

s = Student("Ms Khoo", 'F')
print("=== First view ===")
print(s)

s.set_mark(100)
print("=== Second view ===")
print(s)
