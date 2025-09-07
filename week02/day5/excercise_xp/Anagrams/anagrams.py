# Now create another Python file, called anagrams.py.
# This will contain all the UI (user interface) functionality
# of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit.
# Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input,
# and then be validated:
# Only a single word is allowed.
# If the user typed more than one word, show an error message.
# (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:
#
# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.

import os
from anagram_checker import AnagramChecker


# --- Helpers for input cleaning & validation ---

def clean_input(text: str) -> str:
    """Trim leading/trailing whitespace."""
    return text.strip()


def is_single_alpha_word(text: str) -> bool:
    """True if text is exactly one word and only letters."""
    parts = text.split()
    return len(parts) == 1 and parts[0].isalpha()


def main() -> None:
    # Locate sowpods.txt next to this file
    base_dir = os.path.dirname(os.path.realpath(__file__))
    wordlist_path = os.path.join(base_dir, "sowpods.txt")

    # Create an AnagramChecker instance and apply it to the steps created above.
    checker = AnagramChecker(wordlist_path)

    # Show a menu, offering the user to input a word or exit.
    # Keep showing the menu until the user chooses to exit.
    while True:
        print("\n=== Anagram Checker ===")
        print("1) Enter a word")
        print("2) Exit")
        choice = input("Choose an option (1/2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break
        if choice != "1":
            print("Invalid selection. Please choose 1 or 2.")
            continue

        # If the user chooses to input a word, it must be accepted from the user’s keyboard input,
        raw = input("Enter a single English word: ")
        # Whitespace should be removed from the start and end of the user’s input.
        word = clean_input(raw)

        # Only a single word is allowed.
        # Only alphabetic characters are allowed. No numbers or special characters.
        if not is_single_alpha_word(word):
            print("Error: Please enter exactly ONE word with letters only (A–Z).")
            continue

        # is_valid_word(word) – check if the given word is a valid word.
        if not checker.is_valid_word(word):
            print(f'YOUR WORD: "{word.upper()}"')
            print("This is NOT a valid English word (per SOWPODS).")
            continue

        # All possible anagrams to the user’s word.
        anas = checker.get_anagrams(word)

        # Display the information about the word in a user-friendly message.
        print(f'YOUR WORD: "{word.upper()}"')
        print("This is a valid English word.")
        if anas:
            # Lowercase for nicer display; join with commas.
            print("Anagrams for your word:", ", ".join(a.lower() for a in anas) + ".")
        else:
            print("No anagrams found.")

if __name__ == "__main__":
    main()
