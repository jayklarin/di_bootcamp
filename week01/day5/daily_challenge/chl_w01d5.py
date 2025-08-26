# Daily Challenge: Challenges

# Last Updated: April 30th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll Learn

# Python Basics
# String Manipulation
# Lists
# Sorting
# Functions


# Challenge 1: Sorting



# Instructions:

# Write a Python program that takes a single string of words as input,
# where the words are separated by commas (e.g., ‘apple,banana,cherry’).
# The program should output these words sorted in alphabetical order,
# with the sorted words also separated by commas.

# Step 1: Get Input
unsorted_string = str(input('Enter a string of words separated by commas: '))
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.


# Step 2: Split the String
my_list = unsorted_string.split(',')

# Step 3: Sort the List
my_list.sort()

# Step 4: Join the Sorted List (back into a string)
sorted_string = ",".join(my_list)

# Step 5: Print the Result
# Print the resulting comma-separated string.
print(sorted_string)


# Expected Output:

# If the input is without,hello,bag,world, the output should be bag,hello,without,world.


# Challenge 2: Longest Word



# Instructions:

# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.



# Step 1: Define the Function
the_sentence = "When I am programming with python in the morning, I am happy."
# Define a function that takes a string (the sentence) as a parameter.
def find_longest_word(sentence):
    # Step 2: Split the Sentence into Words
    word_list = sentence.split(' ')
    # Step 3: Initialize Variables
    longest_length = 0
    longest_word = ""
    # Step 4: Iterate Through the Words
    for word in word_list:
        # Step 5: Compare Word Lengths
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word
    # Step 6: Return the Longest Word
    return longest_word
print(find_longest_word(the_sentence))


# Expected Output:

# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".


# Key Python Topics:

# Functions
# Strings
# .split() method
# Loops (for)
# Conditional statements (if)
# String length (len())
