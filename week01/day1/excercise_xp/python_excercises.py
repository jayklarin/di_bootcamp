# 🌟 Exercise 1 : Hello World
print('Hello world\n' * 4)

# 🌟 Exercise 2 : Some Math
print((99**3) * 8)  # ** is exponentiation, ^ is bitwise XOR

# 🌟 Exercise 3 : What Is The Output ?
# >>> 5 < 3        False
# >>> 3 == 3       True
# >>> 3 == "3"     False
# >>> "3" > 3      TypeError (cannot compare str and int in Python 3)
# >>> "Hello" == "hello"  False

# 🌟 Exercise 4 : Your Computer Brand
computer_brand = "MacBook Air"
print(f"I have a {computer_brand} computer.")

# 🌟 Exercise 5 : Your Information
my_name = "Jay"
my_age = 53
my_shoe_size = 44
my_info = f"My name is {my_name}. At {my_age}, I am still active and I rollerblade on precision size {my_shoe_size} skates."
print(my_info)

# 🌟 Exercise 6 : A & B
a = 3
b = 5
if a > b:
    print("Hello World")

# 🌟 Exercise 7 : Odd Or Even
num1 = int(input("Please enter a number: "))
if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

# 🌟 Exercise 8 : What’s Your Name ?
name = input("What is your name? ")
if name == "Jay":
    print("You took my name, give it back!")
else:
    print(f"Hello {name}, nice to meet you!")

# 🌟 Exercise 9 : Tall Enough To Ride A Roller Coaster
height = int(input("What is your height in cm? "))
if height > 145:
    print("You are tall enough to ride this ride!")
else:
    print("You need to grow some more before you can ride this ride.")
