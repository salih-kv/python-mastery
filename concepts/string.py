# Multiline string is created by using triple single (''') or triple double quotes (""").
multiline_string = '''lorem ipsum dolor sit amet, consectetur adipiscing elit.
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, ea commodo consequat.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """lorem ipsum dolor sit amet, consectetur adipiscing elit.
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, ea commodo consequat.."""
print(multiline_string)

# String Concatenation
first_name = 'John'
last_name = 'Doe'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # John Doe
# Checking the length of a string using len() built-in function
print(len(first_name))  # 4
print(len(last_name))   # 3
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 8

# Escaping special characters
string = '\''
tab = '\tHelp me'
new_line = '\nI am new line\n'

print(string)   # '
print(tab)      #        Help me
print(new_line) # I am new line

# String formatting
name = 'Alice'
age = 25
is_married = True
message = f'Hello, {name}! You are {age} years old and {"married" if is_married else "single"}.'
print(message)

first_name = 'John'
last_name = 'Doe'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
formated_string_new = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string_new)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
# 4 + 3 = 7
# 4 - 3 = 1
# 4 * 3 = 12
# 4 / 3 = 1.33
# 4 % 3 = 1
# 4 // 3 = 1
# 4 ** 3 = 64

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
frmtted_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(frmtted_string)

# Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# start from right end we can use negative indexing. -1 is the last index.
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing Python Strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto