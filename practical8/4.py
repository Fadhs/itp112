try:
    number_file = open('numbers.txt', 'r')
    sum = 0
    count = 0
    for number in number_file:
        sum += int(number)
        count += 1
except IOError:
    print('File cannot be found')
except ValueError:
    print('Invalid integer')
except:
    print('An unknown error occured')
else:
    print('There are {} numbers, and their sum is {}'.format(count, sum))
