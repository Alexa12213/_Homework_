import random

class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)

    def meow(self):
        print(f"{self.name} says: Meow!")

    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours.")
        self.energy += hours
        print(f"{self.name}'s energy level is now {self.energy}.")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")
        self.hunger -= 2
        print(f"{self.name}'s hunger level is now {self.hunger}.")

    def play(self, minutes):
        print(f"{self.name} is playing for {minutes} minutes.")
        self.energy -= minutes
        self.hunger += 1
        print(f"{self.name}'s energy level is now {self.energy}.")
        print(f"{self.name}'s hunger level is now {self.hunger}.")

my_cat = Cat(name="Komi", color="white", age=3)

my_cat.meow()
my_cat.sleep(5)
my_cat.eat("fish")
my_cat.play(10)