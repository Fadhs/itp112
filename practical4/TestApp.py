#important is to recap while loop

import Person as p
import Lecturer as l
import Student as s

name = input("Enter Lecturer Name: ")
nric = input('Enter Lecturer NRIC: ')


while True:
    staffid = input('Enter Staff Id: ')
    if staffid == nric:
        break

hour = float(input('Enter Total Teaching Hour:'))
lecturer1 = l.Lecturer(name, nric, staffid, hour)


name = input("Enter Student Name: ")
nric = input('Enter Student NRIC: ')
adminNo = input('Enter Student Admin No: ')

test = -1
while test <0 or test >100:
    test = float(input('Enter Test mark:'))

exam = -1
while exam <0 or exam >100:
    exam = float(input('Enter Exam mark:'))

student1 = s.Student(name, nric, adminNo)
student1.set_test_mark(test)
student1.set_exam_mark(exam)

print(lecturer1.get_name()+ ", Staff Id: " + lecturer1.get_staff_id() + " earns $%.2f" %(lecturer1.computeSalary()))
print(student1.get_name()+ ", Admin No: " + student1.get_admin_no() + " final mark is %.2f" %(student1.computeFinalMark()))


