myfile = open('myfile.txt', 'r')
name = myfile.readline()
weight = float(myfile.readline())
height = float(myfile.readline())
print('{} has a bmi of {}'.format(name.strip(), weight / height **2))
