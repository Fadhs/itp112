s = input('Enter list of numbers: ')
list = s.split()
max = 0
max2 = 0
for v in list:
    i = int(v)
    if i > max:
        max2 = max
        max = i
    elif i > max2 and i < max:
        max2 = i
print(max2)

