# from baseplayer import BasePlayer
from .baseplayer import BasePlayer
# from .context import BasePlayer

class Player(BasePlayer):
    def __init__(self, balance):
        super().__init__()
        self.balance = balance


    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.balance!r})")
