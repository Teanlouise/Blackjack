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

# Import the random module to shuffle the deck prior to dealing.
import random

# Declare variables to store suits, ranks and values.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Finally, declare a Boolean value to be used to control while loops.
playing = True


class Card:
    """ A card has a suit and a rank."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # String in the format "RANK of SUIT"
        return self.rank + ' of ' + self.suit


class Deck:
    """ A deck holds all cards and can be shuffled. All 52 unique card objects
    need to be initiated and added to a list.
    """

    def __init__(self):
        # Start with an empty list
        self.deck = []
        # Add each card to the list
        for suit in suits:
            for rank in ranks:
                # Build a card for each suit and rank
                self.deck.append(Card(suit, rank))
        # Shuffle the deck
        self.shuffle()

    def __str__(self):
        # Start with an empty string
        deck_str = ''
        # Add each card's string to above
        for card in self.deck:
            deck_str += '\n' + card.__str__()
        # Return the string now containing all the cards
        return deck_str

    def shuffle(self):
        # Use random to shuffle the deck
        random.shuffle(self.deck)

    def deal(self):
        # Remove the top card from the hand and return
        return self.deck.pop()


class Hand:
    """ A hand holds the cards that have been dealt to a player from the deck.
    It also calculates the value of the those cards and adjusts for aces when
    appropriate.

    """
    def __init__(self, deck):
        self.cards = []  # start with an empty list
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces
        self.deck = deck

        self.add_card(self.deck.deal())
        self.add_card(self.deck.deal())

    def add_card(self, card):
        # Add a card to the hand
        self.cards.append(card)
        # Add new cards value, according to rank, to the hand sum
        self.value += values[card.rank]

        # Keep track of how many aces are in the hand
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # Check if there are aces in the hand and the player has bust
        while self.aces and self.value > 21:
            # Yes, so change the value of the ace to 1 instead of 11
            self.value -= 10
            # Remove ace from count as it has been adjusted
            self.aces -= 1
            # Continue to check until there are no aces left in the hand

    def hit(self):
        # Add a new card to the hand from the deck
        self.add_card(self.deck.deal())
        # Check if needs to be adjusted for aces
        self.adjust_for_ace()

    def hit_or_stand(self, round):
        global playing
        # Ask user if they want to hit (pressing any key returns true)
        # or stand (pressing entering will return false)
        playing = bool(input(
            "Do you want to hit (press any key) or stand (press enter)? "))

        if playing:
            # User wants to hit
            self.hit()
            if self.value <= 21:
                # Show cards (but keep one dealer card hidden)
                round.show_hands()

    def __str__(self):
        # start with an empty string
        hand_str = ''
        # start with an empty string
        for card in self.cards:
            hand_str += '\n  '+ card.__str__()
        return 'hand is:' + hand_str


class Chips:
    """Keeps track of a Player's starting chips, bets and ongoing winnings."""

    def __init__(self):
        # Ask user for starting chip amount
        self.total = int(input("How many chips do you want to start with? "))
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self):
        while True:
            try:
                # Ask user for their bet
                self.bet = int(input("How many chips do you want to bet? "))
            except ValueError:
                # User didnt enter an integer
                print("Sorry, a bet must be an integer!")
            else:
                # User entered an integer
                if self.bet > self.total:
                    # User has tried to bet more than their chip total
                    print("Sorry, your bet can't exceed", self.total)
                else:
                    # Bet amount has been set successfully
                    break

    def check_balance(self):
        balance = True
        if self.total <= 0:
            balance = False
            print("Sorry you don't have an chips left!")
        return balance

class Game:
    """The game contains the Player's chips and the deck. """

    def __init__(self):
        self.chips = Chips()
        # Create & shuffle the deck,
        self.deck = Deck()
        self.game_round = 1

    def play_game(self):
        global playing
        # A game has started
        while True:
            # Initiate a new round and play the round
            game_round = Round(self)
            game_round.play_round()

            # Ask to play again
            playing = input(
                "Do you want to play again? Yes (press any key) or No (press Enter)? ")
            balance = self.chips.check_balance()

            if playing and balance:
                # Wants to play again and has a balance
                self.game_round += 1
                continue

            else:
                # Wants to exit
                print("Thanks for playing!")
                break


class Round:
    """ Each game has at least one round. During a round the dealer and player
    are dealt a hand and they take turns until a winner is found.
    """

    def __init__(self, game):
        # Deal two cards to each player
        self.game = game
        self.player = Hand(self.game.deck)
        self.dealer = Hand(self.game.deck)

    def show_hands(self):
        global playing
        # Check if the player has had their turn
        if playing:
            # It's the players turn, so only show one of the dealers card
            print("\nDealer's hand is:\n", self.dealer.cards[0], "\n  <HIDDEN>")
        else:
            # The player has had their turn, show the dealers cards
            print("\nDealer's total is", self.dealer.value, "and", self.dealer.__str__())
        # Always show all of the player's cards
        print("\nPlayer's total is", self.player.value, "and", self.player.__str__())

    def get_the_winner(self):
        chips = self.game.chips
        # Compare the player and dealer's values to find the winner
        if self.player.value > 21:
            # Player busts, player loses bet
            print("--Player busts!--")
            chips.lose_bet()

        elif self.dealer.value > 21:
            # Dealer_busts, player wins bet
            chips.win_bet()
            print("--Dealer busts, Player wins--")

        elif self.dealer.value > self.player.value:
            # Dealer wins, player loses bet
            chips.lose_bet()
            print("--Dealer wins!--")

        elif self.dealer.value < self.player.value:
            # Player wins, player wins bet
            chips.win_bet()
            print("--Player wins!--")

        elif self.dealer.value == self.player.value:
            # There is a tie
            print("--There has been a tie--")

    def play_round(self):
        global playing
        print("--------------------------- ROUND", self.game.game_round, "---------------------------")
        # Prompt the Player for their bet
        self.game.chips.take_bet()

        # Show cards (but keep one dealer card hidden)
        print("\n___STARTING HANDS!___")
        self.show_hands()

        # Player starts
        turn = 1
        while playing:
            # Continue player's turn until STAND or BUST
            print("\n___PLAYER'S TURN (", turn, ")___")
            # Prompt for Player to Hit or Stand
            self.player.hit_or_stand(self)
            turn += 1

            # Check if player has bust
            if self.player.value > 21:
                # Break out of the loop and go to 'game over'
                playing = False

        # If Player hasn't busted, it is Dealers turn
        if self.player.value < 21:
            # Play Dealer's hand until Dealer reaches 17
            while self.dealer.value < 17:
                self.dealer.hit()

        # The game is over(Player has bust or dealer has over 17/bust
        print("\n___RESULT___\n")
        # Announce the winner
        self.get_the_winner()
        # start with an empty string
        self.show_hands()

        # Inform Player of their chips total
        print("\n\nYour chip total is: ", self.game.chips.total)


if __name__ == "__main__":
    # Print an opening statement
    print("Let's play some Black Jack!")
    # Create the game and play
    game = Game()
    Game.play_game(game)