class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def show_title(self):
        print('{} is a {}'.format(self.name, self.title))

class Programmer(Employee):
    def __init__(self, name):
        super().__init__(name, 'Programmer')
        self.skills = []
    def add_skill(self, skill):
        self.skills.append(skill)
    def display_skill(self):
        for skill in self.skills:
            print('{} knows {}'.format(self.name, skill))

class Administrator(Employee):
    def __init__(self, name):
        super().__init__(name, 'Administrator')
        self.skills = []
    def add_skill(self, skill):
        self.skills.append(skill)
    def display_skill(self):
        for skill in self.skills:
            print('{} knows {}'.format(self.name, skill))

e1 = Programmer('John')
e2 = Administrator('James')
e1.add_skill('Python')
e1.add_skill('Java Script')
e2.add_skill('Linux')
e1.display_skill()
e2.display_skill()



