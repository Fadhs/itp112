#important concept is we can have prefix for the initializer. It does not have to be input as a parameter
#this class does not override __str__

import Vehicle

class Skateboard(Vehicle.Vehicle):
    def __init__(self, length = 0):
        Vehicle.Vehicle.__init__(self, initial="SK")
        self.__board_length = length

    def get_board_length(self):
        return self.__board_length

    def __str__(self):
        s= Vehicle.Vehicle.__str__(self)
        s = s + " Length: " + str(self.__board_length)
        return s

