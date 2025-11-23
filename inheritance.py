class prey:
    def flee(self):
        print("fleeing")
class predator:
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


