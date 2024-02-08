from abc import ABC, abstractmethod

class BasePlayer(ABC):
    def __init__(self):
        self.hand = None


    def get_str_hand(self):
        return str(self.hand)


    def hit(self, card):
        self.hand.add_to_hand(card)
