import pytest
from blackjack import BasePlayer, Hand, Card


class ConcretePlayer(BasePlayer):
    pass


@pytest.fixture
def player():
    return ConcretePlayer()


def test_baseplayer_initialization(player):
    assert player.hand is None


def test_baseplayer_get_str_hand(player):
    player.hand = Hand([Card(0, 1), Card(1, 10), Card(2, 3)])   # [Ace of Diamonds, 10 of Hearts, 3 of Clubs]
    rows = ['', '', '', '', '']
    rows[0] += "\t" + " ___  " + "\t" + " ___  " + "\t" + " ___  " + "\n"
    rows[1] += "\t" + f"|{'A'.ljust(2)} | " + "\t" + f"|{'10'.ljust(2)} | " + "\t" + f"|{'3'.ljust(2)} | " + "\n"
    rows[2] += "\t" + f"| {'♦'} | " + "\t" + f"| {'♥'} | " + "\t" + f"| {'♣'} | " + "\n"
    rows[3] += "\t" + f"|_{'A'.rjust(2, '_')}| " + "\t" + f"|_{'10'.rjust(2, '_')}| " + "\t" + f"|_{'3'.rjust(2, '_')}| " + "\n\n"
    assert player.get_str_hand() == "".join(rows)


def test_baseplayer_hit(player):
    player.hand = Hand([])
    card = Card(3, 7)  # 7 of Spades
    player.hit(card)
    assert len(player.hand.cards) == 1
    assert player.hand.cards[0] == card

    card2 = Card(0, 13)  # King of Diamonds
    player.hit(card2)
    assert len(player.hand.cards) == 2
    assert player.hand.cards[1] == card2
