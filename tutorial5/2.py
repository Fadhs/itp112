class Pet:
    def __init__(self, type, name):
        self.name = name
        self.type = type

    def make_sound(self):
        pass

    def move(self):
        print(self.name, 'moves')

    def sleep(self):
        print(self.name, 'sleeps')


class Dog:
    def __init__(self, name):
        super().__init__(self, 'dog', name)

    def make_sound(self):
        print('woof')

    def move(self):
        print(self.name, 'runs')

dog = Dog()
dog.sleep()
dog.move()
