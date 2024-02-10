from pyfiglet import Figlet


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

                End the round with a hand value higher than the dealer's without exceeding 21.
                        > [H]it to take another card.     > [S]tand to stop taking cards.
                The dealer must hit (draw cards) until their hand value is 17 or greater.
                Winning Conditions:
                        ▫ If your hand value exceeds 21, you immediately lose the round, and
                          your bet is forfeited.
                        ▫ If you have a higher hand value than the dealer without busting,
                          you win. Your bet is doubled and returned.
                        ▫ If the dealer has a higher hand value than you without busting,
                          you lose, and the dealer takes your bet.
                        ▫ In a tie between you and the dealer, your original bet is returned
                          to you.
                        ▫ If you're dealt a hand with a value of 21, and the dealer does not,
                          you win 1.5 times your original bet, and the round ends immediately.
                Card Values:
                        ▫ Face cards (King, Queen, Jack) have a value of 10.
                        ▫ Number cards have a value equal to their number.
                        ▫ Aces can be counted as 1 or 11, whichever is more beneficial."""
    )
    print()
