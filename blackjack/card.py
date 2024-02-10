class Card:
    SUIT_SYMBOLS = {
        0: u"\u2666",  # Diamonds
        1: u"\u2665",  # Hearts
        2: u"\u2663",  # Clubs
        3: u"\u2660"  # Spades
    }

    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K"
    }


    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        # Indicate if a card is face-up or face-down
        self.hidden = False


    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.suit!r}, {self.value!r})")


    def __str__(self):
        """Display the playing card with its appropriate suit and value."""
        # Text to display on each row
        rows = ['', '', '', '', '']
        rows[0] += " ___  \n"  # Print the top line of the card.
        if self.hidden:
            rows[1] += "|## | \n"
            rows[2] += "|###| \n"
            rows[3] += "|_##| "
        else:
            rows[1] += f"|{self.VALUE_NAMES[self.value].ljust(2)} | \n"
            rows[2] += f"| {self.SUIT_SYMBOLS[self.suit]} | \n"
            rows[3] += f"|_{self.VALUE_NAMES[self.value].rjust(2, '_')}| "
        return "".join(rows)
