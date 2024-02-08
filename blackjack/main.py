from player import Player
from dealer import Dealer
from game import Game

from baseplayer import BasePlayer

from pyfiglet import Figlet


STARTING_BALANCE = 1000


def main():
    player = Player(STARTING_BALANCE)
    dealer = Dealer()
    game = Game(player, dealer)

    # Display welcome message
    display_banner()
    # Start the game engine
    game.start_game()


def display_banner():
    """Show the game information and rules."""
    # Render game title with ASCII art
    figlet = Figlet()
    figlet.setFont(font="chunky")
    print(
        "       ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦"
    )
    print(figlet.renderText("                         Blackjack"))
    print(
        """                                                               - Ng Wan Ying (c) 2024.
       ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦ ~ ♠ ~ ♥ ~ ♣ ~ ♦

                🎯 Objective: The goal is to end the round with a hand value higher than
                              the dealer's without exceeding 21. Hit to take another card.
                              Stand to stop taking cards.
                🃏 Card Values:
                        ▫ Face cards (King, Queen, Jack) have a value of 10.
                        ▫ Number cards have a value equal to their number.
                        ▫ Aces can be counted as 1 or 11, whichever is more beneficial.
                💥 Bust: If your hand value exceeds 21, you immediately lose the round,
                         and your bet is forfeited.
                🤝 Dealer Rules: The dealer must hit (draw cards) until their hand value
                                 is 17 or greater.
                🏆 Winning Conditions:
                        ▫ If you have a higher hand value than the dealer without busting,
                          you win. Your bet is doubled and returned.
                        ▫ If the dealer has a higher hand value than you without busting,
                          you lose, and the dealer takes your bet.
                        ▫ In a tie between you and the dealer, your original bet is returned
                          to you.
                💯 Natural Blackjack: If you're dealt a hand with a value of 21, and the
                                      dealer does not, you win 1.5 times your original bet,
                                      and the round ends immediately."""
    )
    print()


if __name__ == "__main__":
    main()
