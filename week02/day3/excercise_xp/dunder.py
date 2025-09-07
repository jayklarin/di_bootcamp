# Exercises XP

# Last Updated: August 5th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll Learn

# Dunder methods (__str__, __int__, __repr__, __add__, __iadd__)
# Modules (importing and using)
# string module
# datetime module
# faker module


# 🌟 Exercise 1: Currencies

# Goal: Implement dunder methods for a Currency class to handle string representation,
# integer conversion, addition, and in-place addition.



# Key Python Topics:

# Dunder methods (__str__, __repr__, __int__, __add__, __iadd__)
# Type checking (isinstance())
# Raising exceptions (raise TypeError)


# Instructions:
'''
class Currency:
    def __init__(self, currency, amount):
        if not isinstance(currency, str):
            raise TypeError("currency must be a string")
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        self.currency = currency
        self.amount = amount

    # Using the code above, implement the relevant methods and dunder methods which
    # will output the results below.
    # Worried I will get to many plural "s" values
    def __str__(self) -> str:
        unit = self.currency
        if self.amount != 1 and not unit.endswith('s'):
            unit += 's'
        return f"{self.amount} {unit}"

    def __repr__(self) -> str:
        # Match comment expectation: same as printed string (e.g., '5 dollars')
        return str(self)

    # Allows int(c1)
    def __int__(self):
        return int(self.amount)

    # Allows print(c1 + 5)
    def __add__(self, other):
        # Add Currency + Currency (must share same label) -> numeric result per comments
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount

        # Add Currency + number -> numeric result per comments
        if isinstance(other, (int, float)):
            return self.amount + other

        return NotImplemented

    def __iadd__(self, other):
        # Add Currency += Currency (must share same label)
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self

        # Add Currency += number
        if isinstance(other, (int, float)):
            self.amount += other
            return self

        return NotImplemented

# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# 🌟 Exercise 2: Import

# Goal: Create a module with a function and import it into another file.



# Instructions:

# Create a func.py file with a function that sums two numbers and prints the result.
# Then, import and call the function from exercise_one.py.



# Key Python Topics:

# Modules (creating and importing)
# Functions


# Step 1: Create func.py

# Create a file named func.py.
# Define a function inside that file that takes two numbers as arguments, sums them, and prints the result.


# Step 2: Create exercise_one.py

# Create a file named exercise_one.py.
# Import the function from func.py using one of the import syntaxes provided in the instructions.
# Call the imported function with two numbers.

'''
# 🌟 Exercise 3: String Module

# Goal: Generate a random string of length 5 using the string module.



# Instructions:

# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.



# Key Python Topics:

# string module
# random module
# String concatenation


# Step 1: Import the string and random modules

# Import the string and random modules.
import string
import random
from datetime import datetime


# Step 2: Create a string of all letters
all_letters = string.ascii_letters

# Step 3: Generate a random string
rnd_str = ""
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.
for c in range(0,6):
    random_index = random.randint(0,51)
    rnd_str += all_letters[random_index]
print(rnd_str)


# 🌟 Exercise 4: Current Date

# Goal: Create a function that displays the current date.



# Key Python Topics:

# datetime module


# Instructions:

# Use the datetime module to create a function that displays the current date.

# Step 1: Import the datetime module
import datetime
# Step 2: Get the current date
todays_date = datetime.date.today()
# Step 3: Display the date
print(todays_date)


# 🌟 Exercise 5: Amount Of Time Left Until January 1st

# Goal: Create a function that displays the amount of time left until January 1st.



# Key Python Topics:

# datetime module
# Time difference calculations


# Instructions:

# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module
import datetime
# Step 2: Get the current date and time
def time_until_jan_01():
    current_dt = datetime.datetime.now()
    current_year = current_dt.year
    # Step 3: Create a datetime object for January 1st of the next year
    next_jan_01 = datetime.datetime(current_year+1,1,1)

    # Step 4: Calculate the time difference
    delta = next_jan_01 - current_dt
    day_diff = delta.days

    # Step 5: Display the time difference
    print(day_diff)
# time_until_jan_01()



# 🌟 Exercise 6: Birthday And Minutes

# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method


# Instructions:

# Create a function that accepts a birthdate as an argument
# (in the format of your choice), then displays a message stating
# how many minutes the user lived in his life.
from datetime import datetime

def minutes_lived(birthday):
    current_dt = datetime.now()
    date_object = datetime.strptime(birthday, '%Y-%m-%d')f
    delta = current_dt - date_object
    min_lived = int(delta.total_seconds() / 60)
    print(f'You have lived {min_lived:,} minutes')

minutes_lived('1971-11-09')


# 🌟 Exercise 7: Faker Module

# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# Read more about this module HERE



# Key Python Topics:

# faker module
# Dictionaries
# Lists
# Loops


# Instructions:

# Install the faker module and use it to create a list of dictionaries,
# where each dictionary represents a user with fake data.

# Step 1: Install the faker module

# Step 2: Import the faker module
from faker import Faker
fake = Faker()
# Step 3: Create an empty list of users
users = []

# Step 4: Create a function to add users

# Create a function that takes the number of users to generate as an argument.
def add_users(user_count):
    # Inside the function, use a loop to generate the specified number of users.
    for _ in range(user_count):
        # For each user, create a dictionary with the keys name, address, and language_code.
        user = {
            "name": fake.name(),               # Generate a fake full name
            "address": fake.address(),         # Generate a fake address
            "language_code": fake.language_code()  # Generate a fake language code
        }
        users.append(user)


    # Use the faker instance to generate fake data for each key:
    # name: faker.name()
    # address: faker.address()
    # language_code: faker.language_code()
    # Append the user dictionary to the users list.
# Step 5: Call the function and print the users list
add_users(5)

for u in users:
    print(u)
