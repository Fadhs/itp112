class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

class Employee(Person):
    def __init__(self, name, id):
        Person.__init__(self, name)
        self.__id = id
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def shout(self):
        print('I am employee')

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.__department = department
    def get_department(self):
        return self.__department
    def set_department(self, department):
        self.__department = department

class Executive(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department
    def shout(self):
        super().shout()
        Employee.shout(self)
        print('I am Executive')

ex = Executive('John', 'x123', 'Sales')
ex.shout()
