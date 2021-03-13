# 10.1
class Thing():
    pass

example = Thing()

print(Thing)
print(example)

# 10.2
class Thing2():
    letters = 'abc'

print(Thing2.letters)

# 10.3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

# print(Thing3.letters) >> error!

example2 = Thing3()

print(example2.letters)

# 10.4
class Element():
    def __init__(self, name, symbol, number):
        #+ 10.8
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    #+ 10.6
    def dump(self):
        print(self.name, self.symbol, self.number)
    #+ 10.7
    def __str__(self):
        return str(self.name) + str(self.symbol) + str(self.number)
    #+ 10.8
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number


hydro = Element('Hydrogen', 'H', 1)

# 10.5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**el_dict)

# 10.6
hydrogen.dump()

# 10.7
print(hydrogen)

# 10.8
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# 10.9
class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

gom = Bear()
tokki = Rabbit()
shop = Octothorpe()

print(gom.eats())
print(tokki.eats())
print(shop.eats())

# 10.10
class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone
    
    def does(self):
        print(f"{self.laser.does()} {self.claw.does()} {self.smartphone.does()}")

laser = Laser()
claw = Claw()
smart = SmartPhone()

Robot(laser, claw, smart).does()
