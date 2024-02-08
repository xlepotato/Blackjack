class Hand:
    def __init__(self, cards):
        self.cards = cards


    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.cards!r})")


    def __str__(self):
        """Display all of the cards in hand."""
        rows = ['', '', '', '', '']
        for card in self.cards:
            row0, row1, row2, row3 = str(card).split("\n")
            rows[0] += "\t" + row0
            rows[1] += "\t" + row1
            rows[2] += "\t" + row2
            rows[3] += "\t" + row3
        return "".join([row + "\n" for row in rows])


    def compute_score(self):
        """Compute card values in hand and return the score."""
        score = 0   # Tally non-Ace cards' values
        ace_count = 0   # Count number of Aces in hand
        for card in self.cards:
            val = card.value
            if val == 1:
                ace_count += 1
            else:
                # Jack, Queen, King to be treated as 10 in card value
                score += min(val, 10)
        return __class__.resolve_aces_in_score(score, ace_count)


    def add_to_hand(self, card):
        """Add a card to hand."""
        self.cards.append(card)


    @staticmethod
    def resolve_aces_in_score(score, aces):
        """Resolve value of Aces during score computation."""
        score += aces
        for _ in range(aces):
            if score + 10 <= 21:
                score += 10
        return score
