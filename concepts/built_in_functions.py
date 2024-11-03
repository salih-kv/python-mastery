print("Hello, World!")  # Output: Hello, World!

print(type(42))            # Output: <class 'int'>
print(type("Hello"))       # Output: <class 'str'>
print(type([1, 2, 3]))     # Output: <class 'list'>

print(len("Python"))       # Output: 6
print(len([1, 2, 3, 4]))   # Output: 4

name = input("Enter your name: ")
print("Hello, " + name)

print(int("10") + 5)       # Output: 15
print(float("3.14") * 2)   # Output: 6.28
print(str(100) + " is a string now")  # Output: 100 is a string now

numbers = [1, 2, 3, 4]
print(sum(numbers))        # Output: 10

numbers = [5, 10, 3, 8]
print(max(numbers))        # Output: 10
print(min(numbers))        # Output: 3

numbers = [5, 3, 8, 1]
print(sorted(numbers))     # Output: [1, 3, 5, 8]

print(abs(-10))            # Output: 10
print(abs(5.5))            # Output: 5.5

print(round(3.14159, 2))   # Output: 3.14
print(round(5.6789))       # Output: 6

# enumerate() - Adds a counter to an iterable and returns it as an enumerate object.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# zip() - Combines multiple iterables element-wise into a single iterable of tuples.
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 22]
print(list(zip(names, ages)))
# Output: [('Alice', 24), ('Bob', 30), ('Charlie', 22)]

# unzipping
zipped = [('Alice', 24), ('Bob', 30), ('Charlie', 22)]
names, ages = zip(*zipped)
print(names)  # Output: ('Alice', 'Bob', 'Charlie')
print(ages)   # Output: (24, 30, 22)

# map() - Applies a function to every item in an iterable.
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)             # Output: [1, 4, 9, 16]

# Filters items in an iterable based on a function that returns True or False.
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)        # Output: [2, 4]

# Generates a sequence of numbers
for i in range(3):
    print(i)
# Output:
# 0
# 1
# 2

# all() returns True if all elements are True; any() returns True if at least one element is True.
values = [True, True, False]
print(all(values))         # Output: False
print(any(values))         # Output: True

# Checks if an object is an instance of a specified class.
print(isinstance(10, int))         # Output: True
print(isinstance("Hello", str))    # Output: True
print(isinstance(3.14, float))     # Output: True

# Returns the unique identifier (also known as the "memory address") of an object.
x = 10
print(id(x))               # Output: (unique identifier of x)

# check if an object is an instance of any type within a tuple of types
value = "Hello"
print(isinstance(value, (int, str, float)))  # Output: True
print(isinstance(value, (int, float)))  # Output: False


