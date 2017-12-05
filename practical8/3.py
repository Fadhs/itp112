number_file = open('numbers.txt', 'r')
sum = 0
count = 0
for number in number_file:
    sum += int(number)
    count += 1
print('There are {} numbers, and their sum is {}'.format(count, sum))
