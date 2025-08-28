# Exercises XP

# Last Updated: August 5th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll Learn

# Classes and Objects
# Object instantiation
# Methods
# Attributes


# 🌟 Exercise 1: Cats

# Key Python Topics:

# Classes and objects
# Object instantiation
# Attributes
# Functions


# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.



# Step 1: Create Cat Objects

# Use the Cat class to create three cat objects with different names and ages.


# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.


# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.


# Example:

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# # Step 1: Create cat objects
# # cat1 = create the object

# # Step 2: Create a function to find the oldest cat
# def find_oldest_cat(cat1, cat2, cat3):
#     # ... code to find and return the oldest cat ...

# # Step 3: Print the oldest cat's details

class Cat:
    def __init__(self, cat_name, cat_age, cat_breed):
        self.name = cat_name
        self.age = cat_age
        self.breed = cat_breed

cat1 = Cat('Mittens', 8, 'Tabby')
cat2 = Cat('Jynx', 3, 'Siamese')
cat3 = Cat('Kitty', 14, 'Persian')

def find_oldest_cat(cat1, cat2, cat3):
    cat1_age = cat1.age
    cat2_age = cat2.age
    cat3_age = cat3.age
    cat_ages = [cat1_age, cat2_age, cat3_age]
    cat_ages.sort()
    print(cat_ages[-1])
find_oldest_cat(cat1, cat2, cat3)


# 🌟 Exercise 2 : Dogs

# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)


# Instructions:

# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.



# Step 1: Create the Dog Class

# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “ goes woof!”.
# Create a jump() method that prints “ jumps cm high!”, where x is height * 2.

class Dog:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height
    def bark(self):
        print(f'{self.name} goes woof!')
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Step 2: Create Dog Objects

# Create davids_dog and sarahs_dog objects with their respective names and heights.
davids_dog = Dog('Fido',43)
sarahs_dog = Dog('Lady',38)

# Step 3: Print Dog Details and Call Methods

# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.
print(davids_dog.__dict__)
print(sarahs_dog.__dict__)

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()
# Step 4: Compare Dog Sizes
if sarahs_dog.height > davids_dog.height:
    height_diff = sarahs_dog.height - davids_dog.height
    print(f"Sara's dog is {height_diff} cm bigger than David's dog.")
elif davids_dog.height > sarahs_dog.height:
    height_diff = davids_dog.height - sarahs_dog.height
    print(f"David's dog is {height_diff} cm bigger than Sara's dog.")


# 🌟 Exercise 3 : Who’s The Song Producer?

# Goal: Create a Song class to represent song lyrics and print them.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Lists


# Instructions:

# Create a Song class with a method to print song lyrics line by line.



# Step 1: Create the Song Class

# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


# Example:

# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]

class Song:
    def __init__(self,lyrics: list):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for word in self.lyrics:
            print(word)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# 🌟 Exercise 4 : Afternoon At The Zoo

# Goal:

# Create a Zoo class to manage animals. The class should allow adding animals, displaying them,
# selling them, and organizing them into alphabetical groups.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation


# Instructions

# Step 1: Define The Zoo Class

# 1. Create a class called Zoo.
class Zoo:

    # 2. Implement the __init__() method:
    # It takes a string parameter zoo_name, representing the name of the zoo.
    # Initialize an empty list called animals to keep track of animal names.
    def __init__(self, zoo_name) -> None:
        self.zoo_name = zoo_name
        self.animals = []

    # 3. Add a method add_animal(new_animal):
    # This method adds a new animal to the animals list.
    # Do not add the animal if it is already in the list.
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            print(f'{new_animal} has been added to the list')
            self.animals.append(new_animal)
        else:
            print(f'{new_animal} is already on the list')

    # 4. Add a method get_animals():
    # This method prints all animals currently in the zoo.
    def get_animals(self):
        print('Here are all the animals in the zoo')
        for animal in self.animals:
            print(animal)

    # 5. Add a method sell_animal(animal_sold):
    # This method checks if a specified animal exists on the animals list and if so, remove from it.
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            print(f'The {animal_sold} has been sold and removed from the list.')
            self.animals.remove(animal_sold)
        else:
            print(f"Since you don't already own a {animal_sold}, you can't sell it.  The list stays the same.")

    # 6. Add a method sort_animals():
    # This method sorts the animals alphabetically.
    # It also groups them by the first letter of their name.
    # The result should be a dictionary where:
    # Each key is a letter.
    # Each value is a list of animals that start with that letter.
    # Example output:
    # {
    #    'B': ['Baboon', 'Bear'],
    #    'C': ['Cat', 'Cougar'],
    #    'G': ['Giraffe'],
    #    'L': ['Lion'],
    #    'Z': ['Zebra']
    # }
    def sort_animals(self):
        grouped_by = dict()
        self.grouped_by = grouped_by
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_by:
                self.grouped_by[first_letter] = []
            self.grouped_by[first_letter].append(animal)
            print(self.grouped_by)
        return self.grouped_by

    # 7. Add a method get_groups():
    # This method prints the grouped animals as created by sort_animals().
    # Example output:
    # B: ['Baboon', 'Bear']
    # C: ['Cat', 'Cougar']
    # G: ['Giraffe']
    # ...
    def get_groups(self):
        for letter, animals in self.grouped_by.items():
            print(f"{letter}: {animals}")


# Step 2: Create A Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.
zoo1 = Zoo("The Detroit Zoo")

# Step 3: Call The Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.
zoo1.add_animal("Giraffe")
zoo1.add_animal("Lion")
zoo1.add_animal("Bear")
zoo1.add_animal("Dolphin")
zoo1.add_animal("Deer")
zoo1.get_animals()
zoo1.sell_animal('Lion')
zoo1.sort_animals()
zoo1.get_groups()
# Example (No Internal Logic Provided)

# class Zoo:
#     def __init__(self, zoo_name):
#         pass

#     def add_animal(self, new_animal):
#         pass

#     def get_animals(self):
#         pass

#     def sell_animal(self, animal_sold):
#         pass

#     def sort_animals(self):
#         pass

#     def get_groups(self):
#         pass

# # Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()

