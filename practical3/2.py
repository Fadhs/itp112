class Pet:
    types = ['Dog', 'Cat']
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        if animal_type in self.__class__.types:
            self.__animal_type = animal_type
        else:
            print('Pet type', type, 'is not a valid pet type')

    def set_age(self, age):
        self.__age = age

pet = Pet()
name = input('Enter pet name: ')
type = input('Enter pet type: ')
if type not in Pet.types:
    print('Pet type', type, 'is not a valid pet type')
    quit()
age = int(input('Enter age of pet: '))
pet.set_name(name)
pet.set_animal_type(type)
pet.set_age(age)
print('Pet %s is a %s, and it is %d years old' % (pet.get_name(), pet.get_animal_type(),pet.get_age()))
