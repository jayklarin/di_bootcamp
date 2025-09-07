import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        # Example: "A of Hearts"
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        # Initialize a full 52-card deck
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        """Shuffle the deck in place"""
        random.shuffle(self.cards)

    def deal(self):
        """Deal (remove and return) the top card from the deck"""
        if len(self.cards) == 0:
            return None  # No cards left
        return self.cards.pop()  # Removes from the end of the list


# Example usage:
deck = Deck()
print("Initial deck size:", len(deck.cards))  # 52

deck.shuffle()
print("Top 5 cards after shuffle:", deck.cards[:5])

card = deck.deal()
print("Dealt card:", card)
print("Deck size after dealing:", len(deck.cards))  # 51
