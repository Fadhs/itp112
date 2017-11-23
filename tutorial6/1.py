class Shape:
    def __init__(self, side):
        self.side = side
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__(4)
        self.length = length
    def area(self):
        return self.length * self.length

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height
    def area(self):
        return self.height * self.base * 0.5

def display_area(shape):
    if isinstance(shape, Square):
        print('The area of {} is {}'.format('square', shape.area()))
    elif isinstance(shape, Triangle):
        print('The area of {} is {}'.format('triangle', shape.area()))

sq = Square(5)
display_area(sq)
tr = Triangle(5, 6)
display_area(tr)

