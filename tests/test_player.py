import pytest
from blackjack import Player


@pytest.fixture
def player():
    return Player(1000)


def test_player_initialization(player):
    assert player.hand is None
    assert player.balance == 1000


def test_player_repr(player):
    assert repr(player) == "Player(1000)"
