import random

class animal:
    def __init__(self, species, name, age, health, hunger, happieness):
        super().__init__()
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happieness = happieness

    def grow(self):
        self.age += 1
class zoo:
    def __init__(self):
        super().__init__()
        self.animal = []
    def add_animal(self, animal):
            self.animals.append(animal)
            self.health -= random.randint(0, 5)
            self.hunger += random.randint(0, 5)
            self.happiness -= random.randint(0, 5)
    def eat(self):
        if self.hunger >= 6:
            self.health += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
            self.hunger -= random.randint(5, 7)
        else:
            print("NE GOLODEN")

    def play(self):
        self.health -= random.randint(0, 5)
        self.hunger += random.randint(0, 5)
        self.happiness += random.randint(10, 20)



























import random

class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
        self.health = 100
        self.hunger = 0
        self.happiness = 50

    def grow(self):
        self.age += 1
        self.health -= random.randint(0, 5)
        self.hunger += random.randint(0, 5)
        self.happiness -= random.randint(0, 5)

    def eat(self):
        self.health += random.randint(0, 10)
        self.hunger -= random.randint(10, 20)
        self.happiness += random.randint(0, 5)

    def play(self):
        self.health -= random.randint(0, 5)
        self.hunger += random.randint(0, 5)
        self.happiness += random.randint(10, 20)

    def __str__(self):
        return f"{self.species} '{self.name}', age {self.age}, health {self.health}, hunger {self.hunger}, happiness {self.happiness}"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def feed_all(self):
        for animal in self.animals:
            animal.eat()

    def play_with(self):
        for animal in self.animals:
            animal.play()

    def grow_all(self):
        for animal in self.animals:
            animal.grow()

    def __str__(self):
        return f"Zoo ({len(self.animals)} animals)"