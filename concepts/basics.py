# Python:

# No semicolons.
# Indentation defines code blocks instead of { }.
# Comments use #.

# Python - Print "Hello, World!"
print("Hello, World!")

# Python - Variables
name = "Alice"       # string
age = 25             # integer
is_active = True     # boolean

# Python - List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # add item

# Python - Dictionary
person = {"name": "Alice", "age": 25}
print(person["name"])  # Access value

# Python - Function
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# Python - For Loop
for fruit in fruits:
    print(fruit)

# Python - While Loop
i = 0
while i < 5:
    print(i)
    i += 1
    
# Python - Conditional Statements
if age > 18:
    print("Adult")
elif age == 18:
    print("Just turned adult")
else:
    print("Minor")
    
# Python - Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}"

person = Person("Alice", 25)
print(person.greet())

# Python - Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Python - Lambda
add = lambda x, y: x + y
print(add(5, 3))

# Python - Import
import math
print(math.sqrt(16))







