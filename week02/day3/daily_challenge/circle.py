# Daily Challenge - Circle

# Last Updated: April 30th, 2025

# What You Will Learn :

# OOP dunder methods


# Instructions :

# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math

class Circle:
    # A Circle can be defined by either specifying the radius or the diameter.
    def __init__(self, radius=None, diameter=None) -> None:
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter * 0.5
        else:
            print('A radius or a diameter must be selected.')

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius**2)

    def __str__(self) -> str:
        return f"Circle with a radius of {self.radius} has a diameter of {self.diameter} and an area of {self.area}."

    def __add__(self, other):
        # Needs to be encapsulated in Circle to retain all the properties and behaviors
        return Circle(self.radius + other.radius)

    def __eq__(self, other) -> bool:
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=7)

print(c1)
print(c2)
print(c3)

c4 = c1 + c3
print(c4)

print(c1 == c2)
print(c1 > c3)
print(c3 < c4)
circles = [c1, c2, c4, c4]
# sorting
sorted_circles = sorted(circles)
for c in sorted_circles:
    print(c)
