# Welcome to Python Basics tutorial
# Python is a widely used general-purpose, high level programming language.
# It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation.

# Basic Python Programming Tutorial

# 1. Variables and Data Types
print("Variables and Data Types")
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_student = True # Boolean

print("x:", x)
print("y:", y)
print("name:", name)
print("is_student:", is_student)

# 2. Basic Operations
print("\nBasic Operations")
# Arithmetic operations
sum = x + y
difference = x - y
product = x * y
quotient = x / y

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# String concatenation
full_name = name + " Johnson"
print("Full Name:", full_name)

# 3. Lists
print("\nLists")
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])

# Adding and removing items
fruits.append("orange")
print("Fruits after adding orange:", fruits)
fruits.remove("banana")
print("Fruits after removing banana:", fruits)

# 4. Tuples
print("\nTuples")
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)

# 5. Dictionaries
print("\nDictionaries")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Person:", person)
print("Name:", person["name"])

# Adding and removing items
person["email"] = "alice@example.com"
print("Person after adding email:", person)
del person["age"]
print("Person after removing age:", person)

# 6. Conditional Statements
print("\nConditional Statements")
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 7. Loops
print("\nLoops")
# For loop
for fruit in fruits:
    print("Fruit:", fruit)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# 8. Functions
print("\nFunctions")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# 9. Basic Input/Output
print("\nBasic Input/Output")
# Input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# 10. File Operations
print("\nFile Operations")
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

# 11. Exception Handling
print("\nException Handling")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block always executes.")

# 12. Classes and Objects
print("\nClasses and Objects")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

alice = Person("Alice", 25)
print(alice.greet())

# 13. Importing Modules
print("\nImporting Modules")
import math
print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
