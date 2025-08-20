# 🌟 Exercise 1: Favorite Numbers
#
# Key Python Topics:
#
# Sets
# Adding/removing items in a set
# Set concatenation (using union)
#
#
# Instructions:
#
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.
def favorite_numbers():
    my_fav_numbers = {3, 7, 9}
    my_fav_numbers.add(5)
    my_fav_numbers.add(11)
    my_fav_numbers.remove(11)

    friend_fav_numbers = {2, 4, 6, 8}
    our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

    print("My favorite numbers:", my_fav_numbers)
    print("Friend's favorite numbers:", friend_fav_numbers)
    print("Our favorite numbers:", our_fav_numbers)
#favorite_numbers()
#
#
# 🌟 Exercise 2: Tuple
#
# Key Python Topics:
#
# Tuples (immutability)
#
#
# Instructions:
#
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
#
#
# 🌟 Exercise 3: List Manipulation
#
# Key Python Topics:
#
# Lists
# List methods: append, remove, insert, count, clear
#
#
# Instructions:
#
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
#
#
# 🌟 Exercise 4: Floats
#
# Key Python Topics:
#
# Lists
# Floats and integers
# Range generation
#
#
# Instructions:
#
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
#
#
# 🌟 Exercise 5: For Loop
#
# Key Python Topics:
#
# Loops (for)
# Range and indexing
#
#
# Instructions:
#
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.
#
#
# 🌟 Exercise 6: While Loop
#
# Key Python Topics:
#
# Loops (while)
# Conditionals
#
#
# Instructions:
#
# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.
#
#
# 🌟 Exercise 7: Favorite Fruits
#
# Key Python Topics:
#
# Input/output
# Strings and lists
# Conditionals
#
#
# Instructions:
#
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"
#
#
# 🌟 Exercise 8: Pizza Toppings
#
# Key Python Topics:
#
# Loops
# Lists
# String formatting
#
#
# Instructions:
#
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.
#
#
# 🌟 Exercise 9: Cinemax Tickets
#
# Key Python Topics:
#
# Conditionals
# Lists
# Loops
#
#
# Instructions:
#
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.
#
#
# Bonus:
#
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.
#
# 🌟 Exercise 10: Sandwich Orders
#
# Key Python Topics:
#
# Lists
# Loops (while)
#
#
# Instructions:
#
# Using the list:
# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.