class Student:
    _adminNO = ""
    _name = ""
    _gpa = 0.0

    def get_adminNO(self):
        print("Admin No: ", self._adminNO)

    def get_name(self):
        return self._name

    def get_gpa(self):
        return self._gpa

    def display(self):
        print("Name: ", self._name)
        print("GPA: ", self._gpa)

s1 = Student()
print('Name: ', s1._name)
print('GPA: ', s1._gpa)
print('Admin No: ', s1._adminNO)
