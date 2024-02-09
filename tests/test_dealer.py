import pytest
from blackjack import Dealer


@pytest.fixture
def dealer():
    return Dealer()


def test_dealer_initialization(dealer):
    assert dealer.hand is None


def test_dealer_repr(dealer):
    assert repr(dealer) == "Dealer()"
