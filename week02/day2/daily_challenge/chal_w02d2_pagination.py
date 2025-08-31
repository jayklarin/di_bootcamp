# Daily Challenge : Pagination

# Last Updated: May 5th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll Learn

# Classes and Objects
# Method chaining
# List slicing and indexing
# Error handling
# Type conversion


# Key Python Topics:

# Classes and Objects
# Constructors and instance attributes
# List slicing and indexing
# Method chaining (return self)
# Type casting (int())
# Conditional logic
# Custom exceptions


# Instructions: Pagination System

# 📄 What is Pagination?

# In web development, pagination helps break large lists into smaller,
# manageable chunks (pages), making it easier to navigate content like
# search results, product listings, or articles.

# Here’s a visual example:

# Page 1      Page 2      Page 3
# [a, b, c]   [d, e, f]   [g, h, i]


# Goal:

# Create a Pagination class that simulates a basic pagination system.


import math
# Step 1: Create the Pagination Class

# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.
class Pagination:

    # Step 2: Implement the __init__ Method
    # Accept two optional parameters:
    # items (default None): a list of items
    # page_size (default 10): number of items per page
    def __init__(self, items=None, page_size=10) -> None:   # If items is None, initialize it as an empty list.
        # Save page_size and set current_idx (current page index) to 0.
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.page_size = int(page_size)
        self.page_index = 0

    def total_items(self):
        return len(self.items)

    # Calculate total number of pages using math.ceil.
    def total_pages(self):
        if len(self.items) == 0:
            return 0
        return math.ceil(len(self.items) / self.page_size)

    # Step 3: Implement the get_visible_items() Method
    # This method returns the list of items visible on the current page.
    # Use slicing based on the current_idx and page_size.
    def get_visible_items(self):
        if self.total_pages() == 0:
            return []
        start = self.page_index * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def current_idx(self):
        return self.page_index

    # Step 4: Implement Navigation Methods
    # These methods should help navigate through pages:
    # go_to_page(page_num)
    # → Goes to the specified page number (1-based indexing).
    def go_to_page(self, page_num):
        page_num = int(page_num)
        total = self.total_pages()
        if total == 0:
            raise ValueError("No pages available.")
        if page_num < 1:
            self.page_index = 0                 # clamp to first page
        elif page_num > total:
            self.page_index = total - 1         # clamp to last page
        else:
            self.page_index = page_num - 1
        return self


    def first_page(self):
        """Go to the first page (index 0)."""
        self.page_index = 0
        return self

    def last_page(self):
        """Go to the last page (index total_pages-1)."""
        total = self.total_pages()
        self.page_index = total - 1 if total > 0 else 0
        return self

    def next_page(self):
        """Move forward one page unless already at the last page."""
        total = self.total_pages()
        if total > 0 and self.page_index < total - 1:
            self.page_index += 1
        return self

    def previous_page(self):
        """Move back one page unless already at the first page."""
        if self.page_index > 0:
            self.page_index -= 1
        return self

    # 📝 Note:
    # Pages are indexed internally from 0, but user input is expected to start at 1.
    # All navigation methods (except go_to_page) should return self to allow method chaining.


    # Step 5: Add a Custom __str__() Method
    def __str__(self):
        # Show the items on the current page, one per line.
        # If there are no items, return an empty string.
        visible = self.get_visible_items()
        return "\n".join(str(x) for x in visible)

# This magic method should return a string displaying the items on the current page, each on a new line.
# Example:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))
# Output:
# a
# b
# c
# d


# Step 6: Test Your Code

# Use the following test cases:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx() + 1)
# Output: 7

p.go_to_page(0)
# Raises ValueError


