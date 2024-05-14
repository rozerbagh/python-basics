# Class and Object:
# A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that objects of the class will have.
# An object is an instance of a class.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving {self.brand} {self.model}")


car1 = Car("Toyota", "Corolla")
car1.drive()  # Output: Driving Toyota Corolla


# Inheritance:
class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call the constructor of the superclass
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging {self.brand} {self.model}")


e_car1 = ElectricCar("Tesla", "Model S", "100 kWh")
e_car1.drive()  # Output: Driving Tesla Model S
e_car1.charge()  # Output: Charging Tesla Model S


# Encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def change_name(self, new_name):
        self.__name = new_name


person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30
person1.__name  # Error: 'Person' object has no attribute '__name'


# Polymorphism
class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


def animal_sound(animal):
    animal.make_sound()


dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
