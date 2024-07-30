# Object-Oriented Programming
# (OOP) concepts in Python, covering classes, objects, inheritance, polymorphism,
# encapsulation, and more.

# Python OOP Concepts Tutorial

# 1. Classes and Objects
print("Classes and Objects")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object
alice = Person("Alice", 25)
print(alice.greet())

# 2. Inheritance
print("\nInheritance")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_id(self):
        return f"My student ID is {self.student_id}."

# Creating an object of the derived class
bob = Student("Bob", 22, "S12345")
print(bob.greet())
print(bob.get_student_id())

# 3. Polymorphism
print("\nPolymorphism")
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# Polymorphic function
def animal_sound(animal):
    print(animal.sound())

# Creating objects
dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)

# 4. Encapsulation
print("\nEncapsulation")
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount("123456789", 1000)
print("Initial Balance:", account.get_balance())
account.deposit(500)
print("Balance after deposit:", account.get_balance())
account.withdraw(200)
print("Balance after withdrawal:", account.get_balance())

# 5. Abstraction
print("\nAbstraction")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Creating an object
rect = Rectangle(10, 20)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

# 6. Method Overriding
print("\nMethod Overriding")
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

# Creating an object
dog = Dog()
print(dog.speak())

# 7. Method Overloading (Python does not support method overloading, but we can achieve similar behavior)
print("\nMethod Overloading")
class Math:
    def add(self, a, b, c=0):
        return a + b + c

# Creating an object
math = Math()
print("Addition of two numbers:", math.add(1, 2))
print("Addition of three numbers:", math.add(1, 2, 3))

# 8. Class and Static Methods
print("\nClass and Static Methods")
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        return f"Instance variable: {self.instance_variable}"

    @classmethod
    def class_method(cls):
        return f"Class variable: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "I am a static method"

# Creating an object
obj = MyClass("I am an instance variable")
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())
# ```
#
# This tutorial covers:
# - Classes and objects
# - Inheritance
# - Polymorphism
# - Encapsulation
# - Abstraction
# - Method overriding
# - Method overloading (simulated)
# - Class and static methods
#
