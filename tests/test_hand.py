import pytest
from blackjack import Card
from blackjack import Hand


@pytest.fixture
def hand():
    return Hand([Card(0, 1), Card(1, 10), Card(2, 3)])  # Example hand: [Ace of Diamonds, 10 of Hearts, 3 of Clubs]


def test_hand_initialization(hand):
    assert len(hand.cards) == 3
    assert all(isinstance(card, Card) for card in hand.cards)


def test_hand_repr(hand):
    assert repr(hand) == "Hand([Card(0, 1), Card(1, 10), Card(2, 3)])"


def test_hand_str(hand):
    expected_output = (
        "\t ___  \t ___  \t ___  \n"
        "\t|A  | \t|10 | \t|3  | \n"
        "\t| ♦ | \t| ♥ | \t| ♣ | \n"
        "\t|__A| \t|_10| \t|__3| \n\n"
    )
    assert str(hand) == expected_output


def test_hand_compute_score(hand):
    assert hand.compute_score() == 14  # Ace (1) + 10 + 3 = 14
    assert Hand([Card(0, 9), Card(2, 1), Card(1, 1)]).compute_score() == 21 # Ace (11 + 1) + 9 = 21
     # Test hand with face cards
    assert Hand([Card(0, 11), Card(1, 12), Card(2, 13)]).compute_score() == 30  # Jack (10) + Queen (10) + King (10) = 30


def test_hand_add_to_hand(hand):
    new_card = Card(3, 5)  # Add a new card to the hand
    hand.add_to_hand(new_card)
    assert len(hand.cards) == 4
    assert hand.cards[-1] == new_card


def test_hand_resolve_aces_in_score():
    # Test resolving Aces in score computation
    assert Hand.resolve_aces_in_score(10, 0) == 10  # No Aces: 0 + 10 = 10
    assert Hand.resolve_aces_in_score(10, 1) == 21  # One Ace (11): 11 + 10 = 21
    assert Hand.resolve_aces_in_score(15, 2) == 17  # Two Aces (1): 2 + 15 = 17
    assert Hand.resolve_aces_in_score(5, 3) == 18  # Three Aces (11 + 1 + 1): 13 + 5 = 13
    assert Hand.resolve_aces_in_score(20, 3) == 23  # Three Aces (1 + 1 + 1) = 3 + 20 = 23
    assert Hand.resolve_aces_in_score(10, 4) == 14  # Four Aces (1 + 1 + 1 + 1): 4 + 10 = 14


def test_hand_empty_hand():
    h = Hand([])
    assert len(h.cards) == 0
    assert isinstance(h.cards, list)
    assert repr(h) == "Hand([])"
    assert str(h) == "\n\n\n\n\n"
    assert h.compute_score() == 0
