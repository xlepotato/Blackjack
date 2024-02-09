from .deck import Deck
from .hand import Hand

import sys


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()


    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.player!r}, {self.dealer!r})")


    def start_game(self):
        """Start the blackjack game."""
        while self.player.balance > 0:
            # Get the player confirmation to play
            if not self.confirm_start():
                sys.exit(f"You left the game with ${self.player.balance:.2f}.")
            self.start_round()
            self.reset_round()
            print("\n\n")
        # Player ran out of money
        else:
            print("Insufficient money: Please restart the program to try again.")
            sys.exit("Thanks for playing!")


    def confirm_start(self):
        """Return player's response to play the game."""
        print(f"Balance: ${self.player.balance:.2f}")
        while True:
            response = input("Would you like to play? [Y/N]\n").lower()
            if response in ["y", "yes", "n", "no"]:
                break
        return response in ["y", "yes"]


    def start_round(self):
        """Start a new round of blackjack."""
        self.place_bet()
        self.deal_starting_cards()

        # Handle natural blackjack
        if self.is_blackjack():
            return

        player_bust = self.player_turn()
        if player_bust:
            print(f"You lost ${self.bet:.2f}!")
            return

        dealer_bust = self.dealer_turn()
        if dealer_bust:
            self.player.balance += self.bet * 2
            print(f"Dealer busts! You won ${self.bet:.2f}!")
            return

        # Determine winner based on the highest values in hand
        self.determine_winner()


    def place_bet(self, input_func=input):
        """Process the bet amount received from player."""
        while True:
            try:
                bet = float(input_func(f"Place your bet ({self.MINIMUM_BET}-{self.player.balance:.2f}): $"))
            except ValueError:
                print("Invalid amount.")
                continue
            if bet > self.player.balance:
                print("You do not have sufficient funds.")
            elif bet < self.MINIMUM_BET:
                print(f"The minimum bet is ${self.MINIMUM_BET:.2f}.")
            else:
                self.bet = bet
                self.player.balance -= bet
                print(f"Bet: ${self.bet:.2f}\n")
                break


    def deal_starting_cards(self):
        """Deal the starting cards for a round of blackjack."""
        self.player.hand = Hand(self.deck.deal(2))
        self.dealer.hand = Hand(self.deck.deal(2))
        # One of the dealer's card is face-down
        self.dealer.hand.cards[1].hidden = True
        self.display_hands(self.dealer.hand.cards[1].hidden)


    def display_hands(self, hide_dealer_hand):
        """Show both the dealer's and player's cards in their hand."""
        if hide_dealer_hand:
            print("DEALER: ???")
        else:
            print(f"DEALER: {self.dealer.hand.compute_score()}")
        # Display the cards in dealer's hand
        print(self.dealer.get_str_hand())
        print(f"PLAYER: {self.player.hand.compute_score()}")
        # Display the cards in player's hand
        print(self.player.get_str_hand())


    def is_blackjack(self):
        """Handle natural blackjack scenario."""
        if self.player.hand.compute_score() != 21:
            return False
        if self.dealer.hand.compute_score() == 21:
            self.player.balance += self.bet
            print("Both you and the dealer have Blackjack, it's a tie! Your bet is returned.")
            return True
        self.player.balance += self.bet * 2.5
        print(f"Blackjack! You won ${self.bet * 1.5:.2f}!")
        return True


    def player_turn(self):
        """Handle player actions."""
        while True:
            hit = self.get_player_move()
            if not hit:
                break
            new_card = self.deck.deal(1)[0]
            self.player.hit(new_card)
            print(f"You drew a {new_card.VALUE_NAMES[new_card.value]} of {new_card.SUIT_SYMBOLS[new_card.suit]}.")
            self.display_hands(self.dealer.hand.cards[1].hidden)
            print()

            if self.player.hand.compute_score() > 21:
                # Player bust
                return True
        # Player did not bust
        return False


    def dealer_turn(self):
        """Handle dealer actions."""
        # Reveal the face-down card
        self.dealer.hand.cards[1].hidden = False
        self.display_hands(self.dealer.hand.cards[1].hidden)

        while self.dealer.hand.compute_score() < 17:
            # Dealer hit
            new_card = self.deck.deal(1)[0]
            self.dealer.hit(new_card)
            print(f"Dealer hits and is dealt with a {new_card.VALUE_NAMES[new_card.value]} of {new_card.SUIT_SYMBOLS[new_card.suit]}.")
            self.display_hands(self.dealer.hand.cards[1].hidden)
            input('Press <Enter> to continue...')
            print("\n\n")
        if self.dealer.hand.compute_score() > 21:
            # Dealer bust
            return True
        # Dealer did not bust
        return False


    def get_player_move(self):
        """Get the player's move."""
        while True:
            print()
            move = input("Move: [H]it or [S]tand\n").lower()
            if move in ["h", "hit", "s", "stand"]:
                break
            print("Invalid move.")
        return move in ["h", "hit"]


    def determine_winner(self):
        """Determine the winner of the round."""
        player_score = self.player.hand.compute_score()
        dealer_score = self.dealer.hand.compute_score()

        if dealer_score < player_score:
            self.player.balance += self.bet * 2
            print(f"You won ${self.bet:.2f}!")
        elif dealer_score > player_score:
            print(f"Dealer wins! You lost ${self.bet:.2f}!")
        else:
            self.player.balance += self.bet
            print("It's a tie! Your bet is returned.")


    def reset_round(self):
        """Reset the current round."""
        # Create a brand new deck with fresh playing cards
        self.deck = Deck()
        # Clear both dealer and player hands
        self.dealer.hand = None
        self.player.hand = None
        # Clear bet amount
        self.bet = None
