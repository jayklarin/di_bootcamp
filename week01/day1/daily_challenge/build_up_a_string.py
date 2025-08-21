import random

def build_up_a_string():
    my_string = input("Type a string that is exactly 10 characters long: ")
    my_string_len = len(my_string)

    if my_string_len > 10:
        print("String too long.\n")
    elif my_string_len < 10:
        print('String not long enough.\n')
    else:
        print('Perfect string.\n')

    print("the first charcter in my string is ",my_string[0])
    print("the last charcter in my string is ",my_string[-1])
    print()
    for i in range(1, my_string_len + 1):
        print(my_string[:i])

    chars = list(my_string)           # turn string into list
    random.shuffle(chars)             # shuffle the list
    jumbled = ''.join(chars)          # rejoin into string
    print("\nJumbled string:", jumbled)

build_up_a_string()