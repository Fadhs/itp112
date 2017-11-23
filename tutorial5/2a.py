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


class Dog(Pet):
    def __init__(self, name):
        super().__init__('dog', name)

    def make_sound(self):
        print('woof')

    def move(self):
        print(self.name, 'runs')

dog = Dog('puppy')
dog.sleep()
dog.move()
