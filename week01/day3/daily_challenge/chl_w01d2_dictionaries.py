# Daily Challenge: Dictionaries
# Last Updated: April 30th, 2025
# 👩‍🏫 👩🏿‍🏫 What You’ll Learn
# Python Basics
# Dictionaries
# Conditionals
# Loops


# Challenge 1: Letter Index Dictionary

# Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).

# Key Python Topics:

# User input (input())
# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation
# Lists

# Instructions:

# 1. User Input:

# Ask the user to enter a word.
# Store the input word in a variable.
# 2. Creating the Dictionary:

# Iterate through each character of the input word using a loop.
# And check if the character is already a key in the dictionary.
# If it is, append the current index to the list associated with that key.
# If it is not, create a new key-value pair in the dictionary.
# Ensure that the characters (keys) are strings.
# Ensure that the indices (values) are stored in lists.
# 3. Expected Output:

# For the input “dodo”, the output should be: {"d": [0, 2], "o": [1, 3]}.
# For the input “froggy”, the output should be: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}.
# For the input “grapes”, the output should be: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}.
def letter_index_dictionary():
    my_word = input("Enter a word: ")
    index_dict = {}
    index = 0  # manual index counter
    for char in my_word:
        if char in index_dict:
            index_dict[char].append(index)
        else:
            index_dict[char] = [index]
        index += 1  # update index
    print(index_dict)  # print the dictionary at each step to show progress
#letter_index_dictionary()



# Challenge 2: Affordable Items

# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.


# Key Python Topics:

# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation (replace())
# Type conversion (int())
# Lists
# Sorting (sorted())

# Instructions:

# 1. Store Data:

# You will be provided with a dictionary (items_purchase) where the keys are the item
# names and the values are their prices (as strings with a dollar sign).
# You will also be given a string (wallet) representing the amount of money you have.
# 2. Data Cleaning:

# 3. Determining Affordable Items:

# 4. Sorting and Output:

# Sort the list of affordable items in alphabetical order.
# If the list is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, return the sorted list.
# 5. Examples:

# Given:
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"


# The output should be: ["Bread", "Fertilizer", "Water"].

# Given:
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"


# The output should be: ["Apple", "Bananas", "Fan", "Honey", "Spoon"].

# Given:
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"


# The output should be: "Nothing".

def affordable_items():
    # Dictionary of items and their prices (as strings with $ and commas)
    items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
    #items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
    #items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}

    # Wallet balance (also as a string with $)
    wallet = "$300"
    #wallet = "$100"
    #wallet = "$1"

    # Clean the wallet string by removing "$" and "," then convert to integer
    wallet_amount = int(wallet.replace("$", "").replace(",", ""))

    # Empty list to store items we can afford
    affordable = []

    # Loop through each item and its price in the dictionary
    for item, price in items_purchase.items():
        # Clean the price string just like we did for the wallet
        # "$1,000" -> "1000" -> 1000
        item_price = int(price.replace("$", "").replace(",", ""))

        # Check if we can afford this item
        if item_price <= wallet_amount:
            # If yes, add it to the list of affordable items
            affordable.append(item)

    # If no items are affordable, print "Nothing"
    if not affordable:
        print("Nothing")
    else:
        # Otherwise, print the items we can afford, sorted alphabetically
        print(sorted(affordable))

affordable_items()
