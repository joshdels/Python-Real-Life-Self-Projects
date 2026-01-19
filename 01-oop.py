# REVIEW CLASSES
# Class is just blueprint's object meaning hollow while the instance is the object itself
# Method is a __init__()
# Attributes


class Employee:
    department = "Hello baby"

    def __init__(self, name, age):
        self.name = name
        self.age = age


employee_first = Employee("Mike", 5)
print(employee_first.name)
print(employee_first.department)


# Instance Method
class Dog:
    species = "Azkalz"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} bro"

    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


my_dog = Dog("Snowpeee", 4)
print(my_dog.description())
print(my_dog.speak("Awooooo"))


# Excercise 1
class Car:

    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"


print(Car("blue", 5000))
print(Car("red", 2000))


# INHERITANCE
# refer to the Parentclass Dog
class Dashshund(Dog):
    pass


class Bulldog(Dog):
    pass


john = Bulldog("John", 5)
print(john.speak("Awoo"))


# Exercises
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


goldy = GoldenRetriever("Goldy", 15)
darky = Dog("Darky", 6)
print(goldy.speak())
print(darky.speak())
