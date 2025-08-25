# Exercises XP

# Last Updated: April 30th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll Learn

# Working with dictionaries
# Loops (for loops)
# Conditionals (if, elif, else)
# Creating and accessing nested data structures



# 🌟 Exercise 1: Converting Lists Into Dictionaries

# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions

# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.



# Lists:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]


# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
def lists_to_dict(keys, values):
    print(dict(zip(keys, values)))

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#lists_to_dict(keys, values)



# 🌟 Exercise 2: Cinemax #2

# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations


# Instructions

# Write a program that calculates the total cost of movie tickets
# for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.



def calculate_ticket_cost(family):
    total_cost = 0
    for name, age in family.items():
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15
        total_cost += price
        print(f"{name.capitalize()} (age {age}): ${price}")
    print(f"Total cost: ${total_cost}")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#calculate_ticket_cost(family)

# Bonus:

# Allow the user to input family members’ names and ages,
# then calculate the total ticket cost.
def input_family_data():
    family = {}
    while True:
        name = input("Enter family member's name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        age = int(input(f"Enter {name}'s age: "))
        family[name] = age
    print(family)
#input_family_data()

# 🌟 Exercise 3: Zara

# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions

# Create and manipulate a dictionary that contains information about the Zara brand.



# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green


# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

def zara_brand():
    brand = {
        "name": "Zara",
        "creation_date": 1975,
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes":  ['men', 'women', 'children', 'home'],
        "international_competitors": ['Gap', 'H&M', 'Benetton'],
        "number_stores": 7000,
        "major_color": {
            "France": 'blue',
            "Spain": 'red',
            "US": ['pink', 'green']
        }
    }
    # Change the value of number_stores to 2.
    brand["number_stores"] = 2
    # Print a sentence describing Zara’s clients using the type_of_clothes key.
    print(f"Zara's clients are: {', '.join(brand['type_of_clothes'])}.")
    # Add a new key country_creation with the value Spain.
    brand["country_creation"] = "Spain"
    # Check if international_competitors exists and, if so, add “Desigual” to the list.
    if "international_competitors" in brand:
        brand["international_competitors"].append("Desigual")
    # Delete the creation_date key.
    brand.pop("creation_date", None)
    # Print the last item in international_competitors.
    print(f"Last international competitor: {brand['international_competitors'][-1]}")
    # Print the major colors in the US.
    print(f"Major colors in the US: {', '.join(brand['major_color']['US'])}")
    # Print the number of keys in the dictionary.
    print(f"Number of keys in the brand dictionary: {len(brand)}")
    # Print all keys of the dictionary.
    print("Keys in the brand dictionary:")
    for key in brand.keys():
        print(key)
#zara_brand()

# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
merge_zara_dicts = {
    "name": "Zara",
    "creation_date": 1975,
    "number_stores": 7000
}

brand = {
        "name": "Zara",
        "creation_date": 1975,
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes":  ['men', 'women', 'children', 'home'],
        "international_competitors": ['Gap', 'H&M', 'Benetton'],
        "number_stores": 7000,
        "major_color": {
            "France": 'blue',
            "Spain": 'red',
            "US": ['pink', 'green']
        }
    }
def zara_merge(dict1, dict2):
    brand.update(merge_zara_dicts)
    print(brand)
#zara_merge(brand, merge_zara_dicts)

# 🌟 Exercise 4: Disney Characters

# Key Python Topics:

# Looping with indexes
# Dictionary creation
# Sorting


# Instructions

# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:



# Character List:

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


# Expected Results:

# 1. Create a dictionary that maps characters to their indices:

# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


# 2. Create a dictionary that maps indices to characters:

# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}


# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:

# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

def disney_characters(users):
    # 1. Characters to indices
    char_to_index = {char: idx for idx, char in enumerate(users)}
    print("Characters to indices:", char_to_index)

    # 2. Indices to characters
    index_to_char = {idx: char for idx, char in enumerate(users)}
    print("Indices to characters:", index_to_char)

    # 3. Sorted characters to indices
    sorted_chars = sorted(users)
    sorted_char_to_index = {char: idx for idx, char in enumerate(sorted_chars)}
    print("Sorted characters to indices:", sorted_char_to_index)
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#disney_characters(users)
