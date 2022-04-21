class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self, pet):
        print(f"{self.first_name} {self.last_name} takes {pet} on a walk")
        self.pet.play()
        return self
    def feed(self, pet, pet_food):
        print(f"{self.first_name} {self.last_name} feeds {pet} his favorite food, {pet_food}!")
        self.pet.eat(pet_food)
        return self
    def bathe(self, pet):
        print(f"{self.first_name} {self.last_name} gives {pet} a nice warm bath!")
        self.pet.noise()
        return self