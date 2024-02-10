import pytest
from blackjack import Deck, Card


@pytest.fixture
def deck():
    return Deck()


def test_deck_initialization(deck):
    assert deck.cards
    assert len(deck.cards) == 52


def test_deck_create_deck(deck):
    assert deck.cards
    assert all(isinstance(card, Card) for card in deck.cards)


def test_deck_shuffle(deck):
    original_order = deck.cards.copy()
    deck.shuffle()
    assert deck.cards != original_order
    assert len(deck.cards) == len(original_order)  # Ensure no cards are lost or added
    assert set(deck.cards) == set(original_order)  # Ensure all cards are still in the deck


def test_deck_deal(deck):
    num_cards_to_deal = 5
    dealt_cards = deck.deal(num_cards_to_deal)
    assert len(dealt_cards) == num_cards_to_deal
    assert len(deck.cards) == 52 - num_cards_to_deal
    assert all(isinstance(card, Card) for card in dealt_cards)
    assert all(card not in deck.cards for card in dealt_cards)


def test_deck_deal_empty_deck(deck):
    # Empty the deck
    while deck.cards:
        deck.cards.pop()
    with pytest.raises(IndexError):     # Pop from empty list
        deck.deal(1)


def test_deck_deal_all_cards(deck):
    # Deal all cards from the deck
    num_cards_to_deal = 52
    dealt_cards = deck.deal(num_cards_to_deal)
    assert len(dealt_cards) == num_cards_to_deal
    assert not deck.cards
    with pytest.raises(IndexError):
        deck.deal(1)

def test_deck_deal_more_cards_than_deck(deck):
    # Try to deal more cards than the deck contains
    with pytest.raises(IndexError):
        deck.deal(53)
