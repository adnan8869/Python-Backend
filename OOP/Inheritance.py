# Single Inheritance Example

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child Class - Inheritance
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Creating objects
animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Buddy")
dog.speak()











# Multi-Level Inheritance Example

# Base class (Level 1)
class Vehicle:
    def start(self):
        print("Vehicle is starting")

# Derived class from Vehicle (Level 2)
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Derived class from Car (Level 3)
class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


vehicle = Vehicle()
vehicle.start()

car = Car()
car.start()
car.drive()

electric_car = ElectricCar()
electric_car.start()
electric_car.drive()
electric_car.charge()
electric_car.drive()
electric_car.charge()
