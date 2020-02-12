"""
Game of BlackJack

Classes:
- Computer Dealer
- Human Player
- 52 cards
- Bank roll
- Game
- Round

Gameplay:
1. Create a bank roll according to user to be used for all subsequent games
2. Start the first round
3. Ask the player for their bet for this round
4. Make sure that the Player's bet does not exceed their available chips
5. Create a deck of 52 cards and shuffle
6. Deal two cards to the Dealer and two cards to the Player
7. Show only one of the Dealer's cards, the other remains hidden
8. Show both of the Player's cards
9. Ask the Player if they wish to Hit, and take another card
10. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
11. If a Player Stands, play the Dealer's hand.
12. The dealer will always Hit until the Dealer's value meets or exceeds 17
13. Determine the winner
14. Adjust the Player's chips accordingly to bank roll
15. Ask the Player if they'd like to play again
16. If so, start again from step 3

Ways for game to end:
1. Player busts (before computer even has a turn)
2. Player goes and stay, computer hits until higher than player but under 21
3. Player goes and stay, computer hits and bust

Rules:
1. Face cards equal 10
2. Aces count as 1 or 11, whichever is preferable

"""
from Chips import Chips
from Deck import Deck
from Round import Round

# Declare variables to store suits, ranks and values.


class Game:
    """The game contains the Player's chips and the deck. """

    def __init__(self):
        # Create & shuffle the deck
        self.deck = Deck()
        self.deck.shuffle()

        self.chips = Chips()

        self.game_round = 1

        # Finally, declare a Boolean value to be used to control while loops.
        self.playing = True

    def play_game(self):
        # A game has started
        self.chips.ask_chips()

        while True:
            # Initiate a new round and play the round
            new_round = Round(self)
            new_round.play_round()

            # Ask to play again
            self.playing = input(
                "Do you want to play again? Yes (press any key) or No (press Enter)? ")

            balance = self.chips.check_balance()

            if self.playing and balance:
                # Wants to play again and has a balance
                self.game_round += 1
                continue

            else:
                # Wants to exit
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    # Print an opening statement
    print("Let's play some Black Jack!")
    # Create the game and play
    game = Game()
    Game.play_game(game)