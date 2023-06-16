from random import randint


class Die:

    def __init__(self, sides=None):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        return x


my_die = Die(6)

for x in range(1,10):
    print('Roll No-' + str(x) + ' dices value ' + str(my_die.roll_die()) )
