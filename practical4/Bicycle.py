#important concept is we can have prefix for the initializer. It does not have to be input as a parameter
# not only __init__ can be override. We can also override __str__

import Vehicle

class Bicycle(Vehicle.Vehicle):
    def __init__(self, gear_count = 1):
        Vehicle.Vehicle.__init__(self, initial="BY")
        self.__gear_count = gear_count

    def __str__(self):
        s= Vehicle.Vehicle.__str__(self)
        s = s + " Gear Count: " + str(self.__gear_count)
        return s
