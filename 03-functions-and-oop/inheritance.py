# Inheritance lets a class reuse and specialize another class.
# Prefer it for a clear "is-a" relationship.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


animals = [Dog("Rex"), Cat("Milo")]
for animal in animals:
    print(animal.name, animal.speak())

# super() calls behavior from the parent class.
class ServiceAnimal(Dog):
    def __init__(self, name, task):
        super().__init__(name)
        self.task = task

    def describe(self):
        return f"{self.name} helps with {self.task}."


service_animal = ServiceAnimal("Buddy", "navigation")
print(service_animal.describe())
