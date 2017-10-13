count = int(input('Enter number of steps: '))
result = []
for i in range(count):
    command = input('Enter command: ')
    list = command.split()
    if list[0] == 'insert':
        result.insert(int(list[1]),int(list[2]))
    elif list[0] == 'print':
        print(result)
    elif list[0] == 'remove':
        result.remove(int(list[1]))
    elif list[0] == 'append':
        result.append(int(list[1]))
    elif list[0] == 'sort':
        result.sort()
    elif list[0] == 'pop':
        result.pop()
    elif list[0] == 'reverse':
        result.reverse()
