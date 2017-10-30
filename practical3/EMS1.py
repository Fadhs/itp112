import Employee as em

employees = {}
command = 0
def display_menu():
    print('Select the program (1-5) to run: ')
    print('1. Search for an employee')
    print('2. Add new employee')
    print('3. Update employee details')
    print('4. Delete and employee')
    print('5. Quit the program')
    command = input('Enter your command (1-5) :')
    return int(command)

def search():
    pass

def add():
    pass

def update():
    pass

def delete():
    pass


while True:
    val = display_menu()
    if val == 5:
        break
    elif val == 1:
        search()
    elif val == 2:
        add()
    elif val == 3:
        update()
    elif val == 4:
        delete()









