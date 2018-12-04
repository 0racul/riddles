from random import choice
from string import ascii_lowercase

__metaclass = type


class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):

    def __init__(self):
      super(Knight, self).__init__()
      self.attack = 7


class Army(Knight):

    def __init__(self):
        super(Knight, self).__init__()
        
        army_amount = 0
        warriors_amount = 0
        knights_amount = 0
        self.warriors_amount = warriors_amount
        self.knights_amount = knights_amount


    def add_units(self, unit_type, amount):

        if unit_type is Warrior:

            for i in range(amount):

                locals()['M' + str(choice(ascii_lowercase) for i in range(5))] = Warrior()

            self.warriors_amount = self.warriors_amount + amount

        elif unit_type is Knight:

            for i in range(amount):

                locals()['M' + str(choice(ascii_lowercase) for i in range(5))] = Knight()

            self.knights_amount = self.knights_amount + amount

        else:
            print('Write down the type and amount through comma')


class Battle(Army):

    def __init__(self):
        super(Army, self).__init__()


    def fight(self, unit_1, unit_2):


        while True:
            unit_2.health = unit_2.health - unit_1.attack
            if unit_2.health <= 0:
                unit_2.is_alive = False
                battle = True
                break
            unit_1.health = unit_1.health - unit_2.attack
            if unit_1.health <= 0:
                unit_1.is_alive = False
                battle = False
                break

        return battle


if __name__ == '__main__':

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")