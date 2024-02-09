import pytest
from blackjack import Card


@pytest.fixture
def card():
    return Card(0, 1)  # Ace of Diamonds


def test_card_initialization(card):
    assert card.suit == 0
    assert card.value == 1
    assert not card.hidden


def test_card_repr(card):
    assert repr(card) == "Card(0, 1)"


def test_card_values_and_suits():
    # Test different card values and suits
    for suit in range(4):
        for value in range(1, 14):
            card = Card(suit, value)
            assert card.suit in range(4)
            assert card.value in range(1, 14)


def test_card_hidden():
    # Test card visibility when face-up and face-down
    card = Card(0, 1)  # Ace of Diamonds
    assert not card.hidden
    card.hidden = True
    assert card.hidden


def test_card_str_face_up(card):
    expected_output = (
        " ___  \n"
        "|A  | \n"
        "| ♦ | \n"
        "|__A| "
    )
    assert str(card) == expected_output


def test_card_str_face_down(card):
    card.hidden = True
    expected_output = (
        " ___  \n"
        "|## | \n"
        "|###| \n"
        "|_##| "
    )
    assert str(card) == expected_output


def test_card_str_invalid_suit():
    # Test invalid suit
    card = Card(4, 1)
    with pytest.raises(KeyError):
        str(card)


def test_card_str_invalid_value():
    # Test invalid value
    card = Card(0, 14)
    with pytest.raises(KeyError):
        str(card)
