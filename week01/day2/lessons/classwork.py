import os

# Clear terminal at the start of the program
os.system('cls' if os.name == 'nt' else 'clear')

'''
numbers = (10, 20, 30, 20, 50)
number2 = tuple(numbers)
print(number2)
print(type(number2))
print(type(numbers))
mixed_tuple = (1, 2.5, 'hello', True)
print(mixed_tuple)
print(type(mixed_tuple))

print(numbers.count(20))  # Count occurrences of 20 in the tuple
print(numbers.index(30))  # Find the index of the first occurrence of 30

fruits = ('apple', 'banana', 'cherry')
vegs = ('carrot', 'broccoli', 'spinach')
combined = fruits + vegs
print(combined)  # Concatenate tuples

a,b,c,d,e = numbers  # Unpack tuple
print(a)
print(b)
print(c)
print(d)
print(e)


my_tuple = ([1, 2, 3], "fixed")
my_tuple[0].append(4)   # ✅ works, modifies the list inside
print(my_tuple)         # ([1, 2, 3, 4], 'fixed')


my_set = set([1, 2, 3, 4, 5])
my_set2 = {6, 7, 8, 9, 10}
print(my_set)
print(type(my_set))
print(my_set2)
print(type(my_set2))

my_list = [1, 2, 3, 4, 5, 2, 3, 4, 5]
print(my_list)
my_set_from_list = set(my_list)  # Convert list to set
print(my_set_from_list)

set1 = {1, 2, 3}
set2 = {3, 4, 5, 1}
print('Set Union')
set_union = set1.union(set2)  # Union of two sets
print(set_union)  # {1, 2, 3, 4, 5}
set_intersection = set1.intersection(set2)  # Intersection of two sets
print('Set Union')
print(set_intersection)
# Difference between two sets
set_difference = set1.difference(set2)
print('Set Difference')
print(set_difference)

def set_colors():
    my_favorite_colors = {'red', 'green', 'blue'}
    friends_favorite_colors = {'orange','pink','green','yellow','red','purple'}
    print('Here is my list')
    print(my_favorite_colors)
    print('Here is my friends list')
    print(friends_favorite_colors)

    common_elements = my_favorite_colors.intersection(friends_favorite_colors)
    print('here are the common elements')
    print(common_elements)
    common_elements.clear()
    print("common elements after clearing")
    print(common_elements)
set_colors()
'''

print('range with one argument, highest number will be the highest number minus one.')
print(list(range(10)))
print('range with two arguments, start at number specified and highest number will be the top number minus one.')
print(list(range(1, 21)))
print('I used the +1 so I could see it stops at 10.')
print(list(range(1, 10+1)))
print('Odds: range with three arguments, start at number specified, highest number will be the top number minus one, and incrament by 2.')
print(list(range(1, 10+1, 2)))
print('Evens: range with three arguments, start at number specified, highest number will be the top number minus one, and incrament by 2.')
print(list(range(2,10+1, 2)))
print('Negative range with one argument, highest number will be the lowest number plus one.')
print(list(range(10, 1-1, -1)))
