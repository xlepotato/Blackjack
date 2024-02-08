import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        # Build the deck
        self.create_deck()
        self.shuffle()


    def __repr__(self):
        return (f"{self.__class__.__name__}()")


    def create_deck(self):
        """Populate the deck with 52 playing cards."""
        for suit in range(4):
            for value in range(1, 14):
                new_card = Card(suit, value)
                self.cards.append(new_card)


    def shuffle(self):
        """Shuffle the cards of a deck."""
        random.shuffle(self.cards)


    def deal(self, num_cards):
        """Remove and return a specified number of cards from the deck."""
        dealt_cards = []
        for _ in range(num_cards):
            # Grab the topmost card from the deck
            drawn_card = self.cards.pop()   # Let the end of the list denotes the top of the deck
            dealt_cards.append(drawn_card)
        return dealt_cards
