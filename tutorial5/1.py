class Pet:
    def __init__(self, type, name):
        self.name = name
        self.type = type
    def make_sound(self):
        pass
    def move(self):
        print(self.name, 'moves')

class Cat(Pet):
    def __init__(self, name):
        super().__init__('cat', name)
    def make_sound(self):
        print('meow')
    def climb(self):
        print(self.name, 'climbs')

