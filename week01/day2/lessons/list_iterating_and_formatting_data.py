import os
import random
import math

# Clear terminal at the start of the program
os.system('cls' if os.name == 'nt' else 'clear')

# The list is first because we plug it into the function
list1 = [5, 10, 15, 20, 25, 50, 20]

def replace_values(lst, change_value, to_value):
    # Replace every occurrence of change_value in lst with to_value.
    # Prints a before/after summary and returns (lst, occurrences).
    print('List before running:')
    print(lst)
    print()

    occurrences = 0
    for i, val in enumerate(lst):
        if val == change_value:
            lst[i] = to_value
            occurrences += 1
            print(f'Found it and changed it at index {i}!')

    if occurrences == 0:
        print("It's not here!")

    print()
    print(f"The value {change_value} was changed to {to_value} a total of {occurrences} times")
    print()
    print('List after running:')
    print(lst)

    return lst, occurrences
#replace_values(list1, 20, 200)

# This is not part of the excercise, but I thought it would be useful.
# I wanted more control over the list used in thd replace_values function.
def create_list(length, num_range, static_num, percentage):
    p = percentage / 100
    lst = []
    # The underscore _ is used because we don't use the value in the loop.
    # It's more pythonic to use it this way.
    for _ in range(length):
        if random.random() < p:
            lst.append(static_num)
        else:
            n = random.randint(1, num_range)
            lst.append(n if n != static_num else (n % num_range) + 1)  # avoid accidental static_num
    return lst
#print(create_list(list_length, number_range, number_to_replace, percentage_to_replace))

# Unpack the following tuple into 4 variables
def unpack_tuple():
    a_tuple = (10, 20, 30, 40)
    a, b, c, d = a_tuple

    print(a)
    print(b)
    print(c)
    print(d)
#unpack_tuple()


# Accept a number from the user and print its multiplication table

def multiplication_table():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        print(f"Multiplication table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Please enter a valid integer.")
#multiplication_table()

# Print the numbers from 1 to 10 using while loop

def print_numbers_while():
    i = 1
    while i <= 10:
        print(i)
        i += 1
#print_numbers_while()

list1 = [5, 10, 15, 20, 25, 50, 20, 20, 45, 70, 20, 90, 100, 20]
list2 = [5, 10, 15, 20, 25, 50, 20]
# Here is a list of the functions defined above
#replace_values(list1, 20, 200)
#print(create_list(list_length, number_range, number_to_replace, percentage_to_replace))
#unpack_tuple()
#multiplication_table()
#print_numbers_while()


# This code is beyond the scope of the exercise, but it demonstrates how to use 
# the first two functions defined above, create_list and replace_values.
list_length = 80
number_range = 100
number_to_replace = 20
number_to_replace_with = 200
percentage_to_replace = 10

semi_random_list = create_list(list_length, number_range, number_to_replace, percentage_to_replace)

replace_values(semi_random_list, number_to_replace, number_to_replace_with)

