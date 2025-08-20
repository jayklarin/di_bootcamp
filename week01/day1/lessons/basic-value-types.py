# Basic Value Types

# String - Strings are immutable
'''
my_name = 'Jay Klarin'

# Check the length
print(len('Jay Klarin'))

# You can access index of string
print(my_name[4])

# Immutabel cannot change letter - causes error
#my_name[0] = 'G'

print(my_name.upper())

student = 'Harry Potter'
student2 = student.replace('Harry', 'Hairless')
print(student2)

print(student.upper())
print(student.lower())
print(student.capitalize())
print(student.title())
description = 'strings are...'
print(description.upper())
description = description.replace('are', 'is')
# Split the string into words and take the first one
first_word = description.split()[0]
print(first_word)

# Numbers - digits that have value that can be calculated
#
my_number = 5
print(my_number + 10)
print(type(my_number+10))
print(my_number * 2)
print(type(my_number *2))
print(my_number / 2)
print(type(my_number/2))
print(my_number - 1)
print(type(my_number-1))
print(my_number ** 2)
print(type(my_number**2))
print(my_number +1.5)
print(type(my_number+1.5))

my_number = 5.0
print(my_number + 10)
print(type(my_number+10))
print(my_number * 2)
print(type(my_number *2))
print(my_number / 2,"should be float")
print(type(my_number/2))
print(my_number - 1)
print(type(my_number-1))
print(my_number ** 2)
print(type(my_number**2))
print(my_number +1.5)
print(type(my_number+1.5))


import math
# Round
print("5.5 rounds to ",round(5.5))
# round up  
print("5.2 rounds up to",math.ceil(5.2)) 
# round down
print("5.6 rounds down to",math.floor(5.6))
'''

# Type Casting
# Convert string to number
my_string = '5'
# print(my_string + 5)  # Error: cannot concatenate str and int
print(my_string + '5')  # Concatenation string to string
print(int(my_string) + 5)  # Addition of numbers
print(float(my_string) + 5)  # Addition with float - operate int with float makes float
print(int(my_string) + 5.0)  # Addition with float

age = '25'
print(int(age) + 10)  # Convert string to int and add 10
print(float(age) + 10)  # Convert string to float and add 10

#convert number to string
my_number = 5
print(str(my_number) + '5')  # Concatenation number to string
print(str(my_number) + '5.0')  # Concatenation number to string
# print(int('THIS IS AN ERROR'))  # Error: cannot convert string to int

#boolean
print(5>7) # False
print(5<7) # True
print(5==7) # False
print(5!=7) # True
print(5>=7) # False
print(5<=7) # True

# General useful note
# Adding types
my_string = 'hello world'
my_string2 = "Python is fun"
print(my_string)  # Print string
print(my_string2)  # Print another string
print(my_string + ' ' + my_string2)  # Concatenation of strings
print('hello world '*5)
print('hello world \n'*5)

# special characters
print('we aren\'t here')  # force apostrophe in string or
print("we aren't here")  # use double quotes
print("we are here \"and\" there")  # force double quotes in string
print('we are here "and" there')  # use single quotes

# f'strings
name = 'Jay'
age = 25
# without f-string 
print('My name is ' + name + ' and I am ' + str(age) + ' years old')  # Concatenation
# with f-string
print(f'My name is {name} and I am {age} years old')

first_name = 'Jay'
last_name = 'Klarin'


#conditional statements
if 5 > 2:
    print('5 is greater than 2')
else:
    print('5 is not greater than 2')

# if-else statement
if first_name == 'Jay':
    print('Hello Jay')
else:
    print('Hello stranger')

# if-elif-else statement
if first_name == 'Jay':
    print('Hello Jay')
elif first_name == 'John':
    print('Hello John')
else:
    print('Hello stranger')