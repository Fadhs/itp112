import random

class Monster:
    def __init__(self, name, health, attack, defence):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence = defence

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_attack(self):
        return self.__attack
    
    def set_attack(self, attack):
        self.__attack = attack

    def get_defence(self):
        return self.__defence
    
    def set_defence(self, defence):
        self.__defence = defence

    def health_damage(self, attack_value):
        damage = attack_value - self.__defence
        self.__health -= damage
        print('{} suffers {} damage, the health is {} now'.format(self.__name, damage, self.__health))
        return self.__health


class FireMonster(Monster):
    def __init__(self):
        super().__init__('firebug', 10, 9, 4)

class WaterMonster(Monster):
    def __init__(self):
        super().__init__('waterbird', 15, 6, 4)

class GrassMonster(Monster):
    def __init__(self):
        super().__init__('grasshopper', 20, 5, 3)

class MonsterGame():
    def __init__(self):
        self.player_monster = self.choose_monster()
        self.computer_monster = self.generate_monster()

    def generate_monster(self):
        choice = random.randint(0,2)
        if choice == 0:
            return FireMonster()
        elif choice == 1:
            return WaterMonster()
        else:
            return GrassMonster()

    def choose_monster(self):
        type = input('Choose your monster (F, W or G): ')
        if type.upper() == 'F':
            return FireMonster()
        elif type.upper() == 'W':
            return WaterMonster()
        elif type.upper() == 'G':
            return GrassMonster()

    def play(self):
        while True:
            health = self.computer_monster.health_damage(self.player_monster.get_attack())
            if health <=0:
                print('You won!')
                break
            health = self.player_monster.health_damage(self.computer_monster.get_attack())
            if health <=0:
                print('You lost!')
                break

def display_info(monster):
    if isinstance(monster, FireMonster):
        print('{} is a Fire Type monster'.format(monster.get_name()))
    elif isinstance(monster, WaterMonster):
        print('{} is a Water Type monster'.format(monster.get_name()))
    elif isinstance(monster, GrassMonster):
        print('{} is a Grass Type monster'.format(monster.get_name()))

m1 = FireMonster()
m2 = WaterMonster()
display_info(m1)
display_info(m2)

game = MonsterGame()
game.play()
