
# 1. Data Structures:

# Python has built-in data structures like lists, tuples, dictionaries, and sets, which are useful for storing and managing data.

# 	Lists: Ordered, mutable, and can hold multiple data types.

my_list = [1, 2, 3, "Python", 4.5]
my_list.append(6)       # Adds an item to the list
print(my_list)          # Output: [1, 2, 3, "Python", 4.5, 6]
print(my_list[0])       # Accesses the first element: Output: 1


# 	Tuples: Ordered, immutable, and can hold multiple data types.

my_tuple = (1, 2, 3, "Python")
print(my_tuple[1])      # Output: 2
# my_tuple[1] = 10      # This will raise an error as tuples are immutable


# 	Dictionaries: Unordered, mutable, and store data in key-value pairs.

my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice
my_dict["age"] = 26     # Update a value
print(my_dict)          # Output: {'name': 'Alice', 'age': 26}


# 	Sets: Unordered, mutable, and store unique elements.

my_set = {1, 2, 3, 4, 4}  # Duplicates are removed
print(my_set)              # Output: {1, 2, 3, 4}
my_set.add(5)
print(my_set)              # Output: {1, 2, 3, 4, 5}



# 2. Control Flow:

# Control flow allows conditional execution of code blocks, looping, and managing repetitive tasks.

# 	If-Else:

x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")


# 	For Loop:

for i in range(5):
    print(i)     # Output: 0 1 2 3 4


# 	While Loop:

count = 0
while count < 5:
    print(count)
    count += 1   # Output: 0 1 2 3 4



# 3. Functions:

# Functions are reusable blocks of code that perform a specific task.

# Defining and Calling a Function:

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


# 	Lambda Function:

square = lambda x: x * x
print(square(5))  # Output: 25


# 	Recursive Function (a function that calls itself):

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120



# 4. Object-Oriented Programming (OOP):

# OOP is a programming paradigm that relies on classes and objects.

# 	Class and Object:

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy")
print(my_dog.name)   # Output: Buddy
print(my_dog.bark()) # Output: Woof!


# 	Inheritance:

class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

my_cat = Cat()
print(my_cat.speak())  # Output: Meow



# 5. Exception Handling:

# Helps manage and handle errors gracefully.

# 	Try-Except Block:

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!


# 	Custom Exception:

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)  # Output: This is a custom error!



# 6. File Handling:

# Reading from and writing to files.

# Writing to a File:

with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading a File:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)






# 7. Iterators and Generators:

# These are used for creating iterable objects. Generators use the yield keyword to produce a series of values.

# 	Iterator:

my_list = [1, 2, 3]
my_iter = iter(my_list)
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2


# Generator:

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)  # Output: 1 2 3



# 8. Modules and Packages:

# Modules and packages help in organizing Python code into manageable sections.

# 	Importing a Module:

import math
print(math.sqrt(16))  # Output: 4.0


# 	Creating and Importing a Custom Module:
# Then, import and use it:

import my_module
print(my_module.greet("Alice"))  # Output: Hello, Alice!


# 	Using pip to Install Packages:

# pip install numpy



# 9. Data Manipulation and Analysis:

# Common operations for handling data like regular expressions and JSON parsing.

# 	Regular Expressions:

import re
text = "The rain in Spain"
match = re.search("rain", text)
if match:
    print("Found")  # Output: Found


# 	Date and Time Operations:

from datetime import datetime
now = datetime.now()
print(now)  # Output: Current date and time


# 	JSON Parsing:

import json
data = '{"name": "Alice", "age": 25}'
parsed_data = json.loads(data)
print(parsed_data["name"])  # Output: Alice