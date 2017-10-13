grades = {'IT1111':90, 'IT1210':81, 'ITP111':60, 'IT1206': 92}
min = 100
module = ''
for key in grades:
    if grades[key] < min:
        module = key
        min = grades[key]
print(module, min)
