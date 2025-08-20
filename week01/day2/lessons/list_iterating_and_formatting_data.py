import os

# Clear terminal at the start of the program
os.system('cls' if os.name == 'nt' else 'clear')

# The list is first because we plug it into the function
list1 = [5, 10, 15, 20, 25, 50, 20]
def replace_values(lst, change_value, to_value):
    """Replace every occurrence of change_value in lst with to_value.
    Prints a before/after summary and returns (lst, occurrences)."""
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

# Example call
#replace_values(list1, 20, 200)



# Example usage:
#replace_values(20, 200)


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


# The functions above can be called here as needed.

list1 = [5, 10, 15, 20, 25, 50, 20, 20, 45, 70, 20, 90, 100, 20]
list2 = [5, 10, 15, 20, 25, 50, 20]
replace_values(list2, 20, 200)

#unpack_tuple()
#multiplication_table()
#print_numbers_while()