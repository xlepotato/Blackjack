from blackjack import Player, Dealer, Game
from blackjack import display_banner


STARTING_BALANCE = 1000


def main():
    player = Player(STARTING_BALANCE)
    dealer = Dealer()
    game = Game(player, dealer)

    # Display welcome message
    display_banner()
    # Start the game engine
    game.start_game()


if __name__ == "__main__":
    main()
