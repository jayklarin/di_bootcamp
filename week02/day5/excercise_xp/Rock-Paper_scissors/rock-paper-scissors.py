# Part II - rock-paper-scissors.py

# Step 6: Implement get_user_menu_choice Function

# Create a function called get_user_menu_choice().
# Display the menu options (“Play a new game”, “Show scores”, “Quit”).
# Get the user’s choice.
# Validate the input (e.g., check if it’s one of the valid options).
# Return the user’s choice.


# Step 7: Implement print_results Function

# Create a function called print_results(results).
# Take a dictionary called results as a parameter (e.g., {"win": 2, "loss": 4, "draw": 3}).
# Print the results in a user-friendly format (e.g., “Wins: 2, Losses: 4, Draws: 3”).
# Thank the user for playing.


# Step 8: Implement main Function

# Create a function called main().
# Pepeatedly show the menu until the user chooses to exit.
# Call get_user_menu_choice() to get the user’s choice.
# If the user chooses to play a game:
# Create a Game object.
# Call the play() method of the Game object.
# Store the result of the game in a dictionary (e.g., results).
# If the user chooses to exit:
# Call print_results() to display the game summary.
# Exit the program.


# Example (Conceptual, No Direct Solution):

# rock-paper-scissors.py
from game import Game


def get_user_menu_choice() -> str:
    # ... code to display menu and get user choice ...
    # ... code to validate user input ...
    # ... code to return user choice ...
    while True:
        print("\n=== Rock–Paper–Scissors ===")
        print("1) Play a new game")
        print("2) Show scores")
        print("3) Quit")
        choice = input("Choose an option (1/2/3): ").strip()
        if choice in {"1", "2", "3"}:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")


def print_results(results: dict) -> None:
    # ... code to print results in a user-friendly way ...
    # ... code to thank user ...
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)
    total = wins + losses + draws
    print("\n=== Results ===")
    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}, Total Games: {total}")
    print("Thanks for playing!\n")


def main() -> None:
    # ... code to call all the related functions depending on the user's choice.
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game = Game()
            outcome = game.play()  # "win", "loss", or "draw"
            if outcome in results:
                results[outcome] += 1

        elif choice == "2":
            print_results(results)

        elif choice == "3":
            print_results(results)
            break


if __name__ == "__main__":
    main()
