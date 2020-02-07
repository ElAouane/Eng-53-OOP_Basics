class Animal():
    #Characteristics
    def __init__(self, legs, eyes, clawse, tasty):
        self.legs = legs
        self.eyes = eyes
        self.claws = clawse
        self.tasty = tasty


    #Behaviours

#Let's create an instance of an Animal object.
animal1 = Animal(legs='8', eyes='8', clawse='25', tasty='No')
print(type(animal1))
print(animal1)

animal2 = Animal(legs='4', eyes='4', clawse='None', tasty='Yes')
print(type(animal2))
print(animal2)