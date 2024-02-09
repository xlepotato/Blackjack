from .baseplayer import BasePlayer

class Dealer(BasePlayer):
    def __init__(self):
        super().__init__()


    def __repr__(self):
        return (f"{self.__class__.__name__}()")
