# Mini-Project - Tic Tac Toe

# Last Updated: July 30th, 2025

# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.



# 👩‍🏫 👩🏿‍🏫 What You’ll Learn

# Conditionals (if, elif, else)
# Loops (for, while)
# Functions
# List manipulation
# User input


# Key Python Topics:

# Lists (2D lists)
# Loops (while)
# Conditional statements (if, elif, else)
# Functions
# User input (input())
# String formatting


# 🛠️ What You Will Create

# A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.



# tic-tac-toe



# Instructions:

# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares
# with their symbol (‘O’ or ‘X’). The first player to get three of their symbols
# in a row (horizontally, vertically, or diagonally) wins. If all squares are
# filled and no player has three in a row, the game is a tie.



# Step 1: Representing the Game Board

# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).
game_board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
    ]

# Step 2: Displaying the Game Board

# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.
def display_board():
    print(game_board[0][0], "|", game_board[0][1], "|", game_board[0][2])
    print("---------")
    print(game_board[1][0], "|", game_board[1][1], "|", game_board[1][2])
    print("---------")
    print(game_board[1][0], "|", game_board[1][1], "|", game_board[1][2])

#display_board()

board_positions = [
    ['00','01','02'],
    ['10','11','12'],
    ['20','21','22']
    ]

def rc_position_key(): # three more underlines
    print(board_positions[0][0], "|", board_positions[0][1], "|", board_positions[0][2])
    print("------------")
    print(board_positions[1][0], "|", board_positions[1][1], "|", board_positions[1][2])
    print("------------")
    print(board_positions[1][0], "|", board_positions[1][1], "|", board_positions[1][2])
rc_position_key()
# Step 3: Getting Player Input

# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.
def player_input(player):
    rc_position_key()  # show the helper board/legend

    while True:
        position = input(f"{player}, enter a position (rowcol, e.g. 01, 12, 22): ").strip()

        # must be exactly two digits
        if len(position) == 2 and position.isdigit():
            r, c = int(position[0]), int(position[1])

            # bounds check
            if 0 <= r <= 2 and 0 <= c <= 2:
                return r, c

        print("Invalid input. Please use two digits 0–2 (e.g., 01, 12, 22).")
#player_input('Player1')


# Step 4: Checking for a Winner

# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.
game_board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
    ]
def check_win(board = game_board, player):
    # check each row

# Step 5: Checking for a Tie

# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.


# Step 6: The Main Game Loop

# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).


# Tips:

# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.
