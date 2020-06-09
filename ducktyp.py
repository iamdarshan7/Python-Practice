# Duck Typing and Easier to ask forgiveness than permission (EAFP)

class Duck:
    def quack(self):
        print('Quack', quack)

    def fly(self):
        print('Flap, Flap!')

class Person:

    def quack(self):
        print('')            