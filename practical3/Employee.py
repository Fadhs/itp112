class Employee:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.department = ''
        self.title = ''
    def __str__(self):
        return '{} (id={}) is a {} from {} department'.format(self.name, self.id, self.title, self.department)
e1 = Employee()
e1.id = 'jdee'
e1.name = 'Jay Dee'
e1.department = 'Sales'
e1.title = 'Manager'
# repeat for the other 2 employee

print(e1)
# print the other 2 employees
