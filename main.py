class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name, "havaet")
class Dog(animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(self.name, 'barkae')
hotdog = Dog("jorik", 3, 'lablador')
print(hotdog.name)
print(hotdog.age)
print(hotdog.breed)
hotdog.eat()
hotdog.bark()