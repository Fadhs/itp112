#important concept is we can have prefix for the initializer. It does not have to be input as a parameter
#this class does not override __str__

import Vehicle

class Skateboard(Vehicle.Vehicle):
    def __init__(self):
        Vehicle.Vehicle.__init__(self, initial="SK")
        self.__board_length = 0



