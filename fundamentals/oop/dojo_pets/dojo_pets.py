from classes.ninja import Ninja
from classes.pets import Pet






finn = Ninja(first_name="Finn", last_name="The Human", pet=Pet(name="Jake", type="Dog", tricks="Becomes Huge", health=100, energy=100), treats=10, pet_food="Pizza")


finn.walk(finn.pet.name).feed(finn.pet.name, finn.pet_food).bathe(finn.pet.name)

