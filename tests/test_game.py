import pytest
from blackjack import Game
from blackjack import Player
from blackjack import Dealer
from blackjack import Hand
from blackjack import Card


# Define test fixtures
@pytest.fixture
def player():
    return Player(1000)


@pytest.fixture
def dealer():
    return Dealer()


@pytest.fixture
def game(player, dealer):
    return Game(player, dealer)


@pytest.fixture
def test_deck():
    return [
        Card(0, 1), Card(1, 2), Card(2, 3), Card(3, 4),  # Sample deck for testing
        Card(0, 5), Card(1, 6), Card(2, 7), Card(3, 8),
        Card(0, 9), Card(1, 10), Card(2, 11), Card(3, 12),
        Card(0, 13), Card(1, 1), Card(2, 2), Card(3, 3),
    ]


# Test cases
def test_game_initialization(game, player, dealer):
    assert game.player == player
    assert game.dealer == dealer
    assert game.bet is None
    assert game.deck


def test_game_confirm_start(game, monkeypatch):
    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: "y")
    assert game.confirm_start() == True
    monkeypatch.setattr('builtins.input', lambda _: "n")
    assert game.confirm_start() == False


def test_game_deal_starting_cards(game, test_deck):
    game.deck.cards = test_deck  # Set the deck to a predefined test deck
    game.deal_starting_cards()
    # Check if both player and dealer have been dealt two cards
    assert len(game.player.hand.cards) == 2
    assert len(game.dealer.hand.cards) == 2
    # Check if the second card of the dealer is hidden
    assert game.dealer.hand.cards[1].hidden


def test_game_determine_winner(game):
    # Set up player and dealer hands
    player_hand = Hand([Card(2, 1), Card(3, 9)])  # Total value: 20
    dealer_hand = Hand([Card(0, 10), Card(1, 7)])   # Total value: 17
    # Set player and dealer hands
    game.player.hand = player_hand
    game.dealer.hand = dealer_hand
    game.bet = 100
    game.player.balance -= game.bet
    # Determine the winner
    game.determine_winner()
    # Check if player's balance is correctly updated (in this case, it should increase by the bet amount)
    assert game.player.balance == 1100

    # Update the player and dealer hands for a different scenario
    player_hand = Hand([Card(0, 11), Card(1, 8)])  # Total value: 18
    dealer_hand = Hand([Card(2, 12), Card(3, 8)])   # Total value: 18
    # Set player and dealer hands
    game.player.hand = player_hand
    game.dealer.hand = dealer_hand
    game.bet = 100
    game.player.balance -= game.bet
    # Determine the winner
    game.determine_winner()
    # # Check if player's balance is correctly updated (in this case, it should not change)
    assert game.player.balance == 1100

    # Update the player and dealer hands for another scenario
    player_hand = Hand([Card(0, 10), Card(1, 5)])  # Total value: 15
    dealer_hand = Hand([Card(2, 6), Card(3, 5), Card(0, 10)])   # Total value: 21
    # Set player and dealer hands
    game.player.hand = player_hand
    game.dealer.hand = dealer_hand
    game.bet = 100
    game.player.balance -= game.bet
    # Determine the winner
    game.determine_winner()
    # Check if player's balance is correctly updated (in this case, it should decrease by the bet amount)
    assert game.player.balance == 1000


def test_game_is_blackjack(game):
    game.dealer.hand = Hand([Card(0, 10), Card(1, 2)])  # Total value: 12
    game.player.hand = Hand([Card(2, 1), Card(3, 10)])  # Total value: 21
    game.bet = 100
    game.player.balance -= game.bet
    assert game.is_blackjack()
    assert game.player.balance == 1150  # Player's hand is natural blackjack

    # Update the player and dealer hands for another scenario (not blackjack)
    game.dealer.hand = Hand([Card(0, 10), Card(1, 2)])  # Total value: 12
    game.player.hand = Hand([Card(2, 1), Card(3, 9)])  # Total value: 20
    game.bet = 100
    game.player.balance -= game.bet
    assert game.is_blackjack() == False
    assert game.player.balance == 1050  # Player's hand is not natural blackjack

    # Update the player and dealer hands for another scenario (both dealer and player blackjack)
    game.dealer.hand = Hand([Card(0, 1), Card(1, 12)])  # Total value: 21
    game.player.hand = Hand([Card(2, 1), Card(3, 11)])  # Total value: 21
    game.bet = 100
    game.player.balance -= game.bet
    assert game.is_blackjack() == True
    assert game.player.balance == 1050  # Both Dealer's and Player's hands are natural blackjack (a tie)


def test_game_reset_round(game):
    game.deck.cards = []  # Set deck to empty
    game.player.hand = Hand([Card(0, 10), Card(1, 2)])  # Add some cards to player's hand
    game.dealer.hand = Hand([Card(2, 1), Card(3, 10)])  # Add some cards to dealer's hand
    game.bet = 0  # Set existing bet to 0
    game.reset_round()  # Reset the round
    assert len(game.deck.cards) == 52  # Deck is replenished
    assert game.player.hand is None  # Player hand is cleared
    assert game.dealer.hand is None  # Dealer hand is cleared
    assert game.bet is None  # Bet amount is reset
