import random

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        randomnum = random.randint(15,25)
        print(f"{self.name} takes a nice long nap to replenish his energy (energy +{randomnum})")
        self.energy += randomnum
        return self
    def eat(self, pet_food):
        randomnum = random.randint(0,10)
        print(f"{self.name} eats their favorite food {pet_food} (health +{randomnum})")
        self.health += randomnum
        return self
    def play(self):
        print(f"{self.name} is feeling playful and {self.tricks}")
        return self
    def noise(self):
        print(f"{self.name} is making noise")
        return self
