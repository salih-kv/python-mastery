# capitalize();
title = "python mastery"
print(title.capitalize())  # Python mastery

# center(width);  # centers the string in the field of width
print("Python".center(20))  #        Python

# count(sub[, start[, end]]);  # counts the number of occurrences of substring
text = "mastering programming language"
print(text.count("m"))  # 3
print(text.count("r", 10, 20))  # 2
print(text.count("age"))  # 1

# endswith(suffix[, start[, end]]);
print("python mastery".endswith("y"))  # True
print("python mastery".endswith("y", 0, 10))  # False

# expandtabs([tabsize]);  # replaces tabs with spaces
print("	Python".expandtabs())  # '    Python'

# find(sub[, start[, end]]);  # finds the index of the first occurrence of substring
text = "mastering programming language"
print(text.find("m"))  # 0
print(text.find("r", 10, 20))  # 11
print(text.find("python"))  # -1 if not found

# rfind(sub[, start[, end]]);  # finds the index of the last occurrence of substring
text = "mastering programming language"
print(text.rfind("g"))  # 28
print(text.rfind("z"))  # -1 if not found

# index(sub[, start[, end]]);  # finds the index of the first occurrence of substring
text = "mastering programming language"
print(text.index("p"))  # 10

# isalnum();  # checks if all characters are alphanumeric
print("123abc".isalnum())  # True
text = 'HundredDaysOfPython'
print(text.isalnum()) # True

text = '100DaysOfPython'
print(text.isalnum()) # True

text = 'hundred days of python'
print(text.isalnum()) # False, space is not an alphanumeric character

text = 'hundred days of python 2024'
print(text.isalnum()) # False

# isalpha();  # checks if all characters are alphabetic
print("123abc".isalpha())  # False
print('HundredDaysOfPython'.isalpha()) # True

# isdigit();  # checks if all characters are digits
print("123abc".isdigit())  # False

# islower();  # checks if all characters are lowercase
print("123abc".islower())  # False

# isspace();  # checks if all characters are whitespace
print("123abc".isspace())  # False

# istitle();  # checks if all characters are titlecase
print("123abc".istitle())  # False

# isupper();  # checks if all characters are uppercase
print("123abc".isupper())  # False

# isnumeric();  # checks if all characters are numeric
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

# isidentifier();  # checks if all characters are valid identifiers
print("123abc".isidentifier())  # False
print("123abc_".isidentifier())  # True
print("_hello".isidentifier())  # True

# join(iterable);  # joins the elements of the iterable with the string as delimiter
fruits = ["apple", "banana", "cherry"]
fruit_str = ",".join(fruits)  # apple,banana,cherry
fruit_str = ",".join(fruits)  # apple,banana,cherry

# strip(chars);  # removes specified characters from the beginning and end of the string
str = "Hello, World!"
stripped_str = str.strip()  # Hello, World!
stripped_str = str.strip("Hello")  # World!

# replace(old, new[, count]);  # replaces all occurrences of substring
str = "Hello, World!"
replaced_str = str.replace("Hello", "Hi")  # Hi, World!
replaced_str = str.replace("World", "Python")  # Hello, Python!
replaced_str = str.replace("World", "Python", 1)  # Hello, Python!

# split([sep[, maxsplit]]);  # splits the string into substrings
text = "Hello, World!"
words = text.split()  # ['Hello', 'World!']
words = text.split(" ")  # ['Hello,', 'World!']
words = text.split(" ", 1)  # ['Hello,', 'World!']

# swapcase();  # swaps the case of all characters
text = "Hello, World!"
swapped_text = text.swapcase()  # hELLO, wORLD!

# startswith(prefix[, start[, end]]);  # checks if the string starts with the specified prefix
text = "Hello, World!"
print(text.startswith("Hello"))  # True
print(text.startswith("World"))  # False