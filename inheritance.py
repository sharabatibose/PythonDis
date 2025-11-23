class Animal:
    def __init__(self, does_eat, does_sleep,):
        does_eat= True
        does_sleep= True
class prey(Animal): #inherits Animal characteristics, then adds characteristics of its own
    def flee(self):
        print("fleeing")
class predator(Animal):
    def hunt(self):
        print("hunting")
class Rabbit(prey):
    def lookcute(self):
        print("looking cute")
class Wolf(predator):
    def lookfierce(self):
        return("looking fierce")
class Fish(prey, predator): #multiple inheritance
    pass
class Tilapia(Fish, Wolf): #multilevel and multiple inheritance
    pass

rab=Rabbit()
rab.flee()
whitewolf=Wolf()
whitewolf.hunt()

tilapia=Tilapia()
print("tilapia is "+tilapia.lookfierce()) 



