import random

class Game:
    # Step 2: Implement get_user_item Method
    # Create a method called get_user_item(self).
    # Ask the user to select an item (rock/paper/scissors).
    def get_user_item(self):
        """Ask the user to choose rock, paper, or scissors and validate input."""
        while True:
            choice = input("Choose rock, paper, or scissors: ").lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            print("Invalid choice. Please try again.")

    # Step 3: Implement get_computer_item Method
    # Create a method called get_computer_item(self).
    # Randomly select an item (rock/paper/scissors).
    # Return the computer’s item.
    def get_computer_item(self):
        """Randomly select rock, paper, or scissors for the computer."""
        return random.choice(["rock", "paper", "scissors"])

    # Step 4: Implement get_game_result Method
    # Create a method called get_game_result(self, user_item, computer_item).
    # Take user_item and computer_item as parameters.
    # Determine the result of the game based on the rules of Rock Paper Scissors.
    # Return “win”, “draw”, or “loss”.
    def get_game_result(self, user_item, computer_item):
        """Determine result: win, draw, or loss."""
        if user_item == computer_item:
            return "draw"

        # Winning conditions for user
        if (
            (user_item == "rock" and computer_item == "scissors")
            or (user_item == "scissors" and computer_item == "paper")
            or (user_item == "paper" and computer_item == "rock")
        ):
            return "win"

        return "loss"

    # Step 5: Implement play Method
    # Create a method called play(self).
    # Call get_user_item() to get the user’s choice.
    # Call get_computer_item() to get the computer’s choice.
    # Call get_game_result() to determine the result.
    # Print the outcome of the game (user’s choice, computer’s choice, result).
    # Return the result (“win”, “draw”, or “loss”) as a string.
    def play(self):
        """Play one round of Rock-Paper-Scissors."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: {result}\n")

        return result
