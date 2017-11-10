import Person

class Lecturer(Person.Person):
    def __init__(self, name, nric, staff_id, totalteachinghr):
        Person.Person.__init__(self, name, nric)
        self.__staff_Id = staff_id
        self.__total_TeachingHour = totalteachinghr

    def get_staff_id(self):
        return self.__staff_Id
    def get_total_teachinghour(self):
        return self.__total_TeachingHour
    def set_staff_id(self, staff_id):
        self.__staff_Id = staff_id
    def set_total_teachinghour(self, totalteachinghr):
        self.__total_TeachingHour = totalteachinghr

    def computeSalary(self):
        return self.__total_TeachingHour*90