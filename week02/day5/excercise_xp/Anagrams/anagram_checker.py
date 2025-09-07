# anagram_checker.py
import os

class AnagramChecker:
    # __init__ - should load the word list file (text file) into a variable,
    # so that it can be searched later on in the code.
    def __init__(self, file_path: str) -> None:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Word list not found: {file_path}")
        # Store all words in a set for O(1) membership tests; normalize to UPPER
        with open(file_path, "r", encoding="utf-8") as f:
            self._words = {line.strip().upper() for line in f if line.strip()}

    # is_valid_word(word) – should check if the given word
    # (ie. the word of the user) is a valid word.
    # Note: method should NOT print; just return True/False.
    def is_valid_word(self, word: str) -> bool:
        if not word or not word.isalpha():
            return False
        return word.strip().upper() in self._words

    # get_anagrams(word) – should find all anagrams for the given word.
    # (eg. if word of the user is ‘meat’, return ["mate","tame","team"])
    # Note: method should NOT print; just return a list.
    def get_anagrams(self, word: str) -> list[str]:
        base = word.strip().upper()
        if not base.isalpha():
            return []
        signature = tuple(sorted(base))  # deterministic key
        # Collect all dictionary words with the same signature, excluding the word itself
        return sorted(
            [w for w in self._words if w != base and tuple(sorted(w)) == signature]
        )

    # Hint method: compare 2 words and return True if they contain the same letters
    # (but not in the same order), and False otherwise.
    # Note: method should NOT print; just return True/False.
    def is_anagram(self, word1: str, word2: str) -> bool:
        a = word1.strip().upper()
        b = word2.strip().upper()
        if not a.isalpha() or not b.isalpha():
            return False
        return a != b and sorted(a) == sorted(b)
