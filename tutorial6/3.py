class Robot:
    population = 0
    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        self.__class__.population += 1
    def die(self):
        print("{} is being destroyed!".format(self.name))
        self.__class__.population -= 1
        if self.__class__.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(self.__class__.population))
    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

def how_many_robots():
        print("We have {:d} robots.".format(Robot.population))

def demo():
    droid1 = Robot("R2-D2")
    droid1.say_hi()
    how_many_robots()

    droid2 = Robot("C-3PO")
    droid2.say_hi()
    how_many_robots()

    print("\nRobots can do some work here.\n")
    print("Robots have finished their work. So let's destroy them.")
    droid1.die()
    droid2.die()

    how_many_robots()

demo()


