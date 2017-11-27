class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

class Student(Person):
    def __init__(self, name, english, math, science):
        super().__init__(name)
        self.__english = english
        self.__math = math
        self.__science = science
    def get_english(self):
        return self.__english
    def get_math(self):
        return self.__math
    def get_science(self):
        return self.__science

class Employee(Person):
    def __init__(self, name, hour, rate):
        super().__init__(name)
        self.__hour = hour
        self.__rate = rate
    def get_hour(self):
        return self.__hour
    def get_rate(self):
        return self.__rate

class AdminModule:
    personList = []

    def __init__(self):
        self.create_instance()

    def create_instance(self):
        s1 = Student('Jane', 75, 80, 85)
        s2 = Student('John', 60, 68, 74)
        s3 = Student('Jerome', 81, 63, 77)
        s4 = Student('Jason', 55, 76, 67)
        s5 = Student('Jessica', 62, 45, 68)
        s6 = Student('Joanne', 52, 47, 51)

        e1 = Employee('Andy', 15, 9)
        e2 = Employee('Amy', 10, 8.5)
        e3 = Employee('Alan', 8, 9)
        e4 = Employee('Anthony', 12, 8.5)
        e5 = Employee('Andrew', 5, 9)

        AdminModule.personList.append(s1)
        AdminModule.personList.append(s2)
        AdminModule.personList.append(s3)
        AdminModule.personList.append(s4)
        AdminModule.personList.append(s5)
        AdminModule.personList.append(s6)

        AdminModule.personList.append(e1)
        AdminModule.personList.append(e2)
        AdminModule.personList.append(e3)
        AdminModule.personList.append(e4)
        AdminModule.personList.append(e5)

    def average_mark(self):
        totalEngligh = 0
        totalMath = 0
        totalScience = 0
        studentCount = 0

        for i in AdminModule.personList:
            if isinstance(i, Student):
                totalEngligh += i.get_english()
                totalMath += i.get_math()
                totalScience += i.get_science()
                studentCount +=1


        print("Average Mark for English is %.2f" %(totalEngligh/studentCount))
        print("Average Mark for MATH is %.2f" %(totalMath / studentCount))
        print("Average Mark for Science is %.2f" %(totalScience / studentCount))

    def highest_mark(self):
        englishMark = 0
        english_student = ""
        mathMark = 0
        math_student = ""
        scienceMark = 0
        science_student = ""

        for i in AdminModule.personList:
            if isinstance(i, Student):
                if i.get_english() > englishMark:
                    englishMark = i.get_english()
                    english_student = i.get_name()
                if i.get_math() > mathMark:
                    mathMark = i.get_math()
                    math_student = i.get_name()
                if i.get_science() > scienceMark:
                    scienceMark = i.get_science()
                    science_student = i.get_name()

        print("Highest Mark for English is %.2f and the student is %s" %(englishMark, english_student))
        print("Highest Mark for Math is %.2f and the student is %s" % (mathMark, math_student))
        print("Highest Mark for Science is %.2f and the student is %s" % (scienceMark, science_student))

    def calculate_salary(self):
        for i in AdminModule.personList:
            if isinstance(i, Employee):
                print("%s salary is $%.2f" %(i.get_name(), (i.get_hour()*i.get_rate())))

    def lowest_salary(self):
        lowest = -1
        lowest_employee = ""
        for i in AdminModule.personList:
            if isinstance(i, Employee):
                salary = i.get_hour()* i.get_rate()
                if lowest_employee == "":
                    lowest = salary
                    lowest_employee = i.get_name()
                elif salary < lowest:
                    lowest = salary
                    lowest_employee = i.get_name()

        print("%s has the lowest salary: $%.2f" % (lowest_employee, lowest))

a = AdminModule()
a.average_mark()
a.highest_mark()
a.calculate_salary()
a.lowest_salary()
