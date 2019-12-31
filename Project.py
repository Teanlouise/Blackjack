"""
Game of BlackJack

Classes:
- Computer Dealer
- Human Player
- 52 cards
- Bank roll

Gameplay:
1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again



Ways for game to end:
1. Player busts (before computer even has a turn)
2. Player goes and stay, computer hits until higher than player but under 21
3. Player goes and stay, computer hits and bust


Rules:
1. Face cards equal 10
2. Aces count as 1 or 11, whichever is preferable

"""

# Step 1: Imports and Global Variables
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
    """Step 2: Create a Card Class - where each Card object has a suit and a rank

    A Card object really only needs two attributes: suit and rank.
    In addition to the Card's __init__ method, add a __str__ method that, when
    asked to print a Card, returns a string in the form "Two of Hearts"
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """Step 3: Create a Deck Class - - hold all 52 cards and can be shuffled
    Here we might store 52 card objects in a list that can later be shuffled.
    First, though, we need to instantiate all 52 unique card objects and add them
    to our list. So long as the Card class definition appears in our code, we can
    build Card objects inside our Deck __init__ method.
    Consider iterating over sequences of suits and ranks to build out each card.

    In addition to an __init__ method we'll want to add methods to shuffle our deck,
    and to deal out cards during gameplay.

    OPTIONAL: We may never need to print the contents of the deck during gameplay,
    but having the ability to see the cards inside it may help troubleshoot any
    problems that occur during development. With this in mind, consider adding a
    __str__ method to the class definition.
    """

    def __init__(self):
        # Start with an empty list
        self.deck = []
        # Add each card to the list
        for suit in suits:
            for rank in ranks:
                # Build a card for each suit and rank
                self.deck.append(Card(suit, rank))

    def __str__(self):
        # Start with an empty string
        deck_str = ''
        # Add each card's string to above
        for card in self.deck:
            deck_str += '\n' + card.__str__()
        # Return the string now containing all the cards
        return deck_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    """ Step 4: Create a Hand Class
    Holds those cards that have been dealt to each player from the deck.

    In addition to holding Card objects dealt from the Deck, the Hand class is
    used to calculate the value of those cards using the values in the
    dictionary defined above.

    It may also need to adjust for the value of Aces when appropriate.

    """
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

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

    def __str__(self):
        hand_str = ''  # start with an empty string
        for card in self.cards:
            hand_str += '\n  '+ card.__str__() # add each Card object's print string
        return 'hand is:' + hand_str


class Chips:
    """ Step 5: Create a Chips Class

    In addition to decks of cards and hands, we need to keep track of a Player's
    starting chips, bets, and ongoing winnings. This could be done using global
    variables, but in the spirit of object oriented programming, let's make a Chips
    class instead!
    """
    def __init__(self):
        # Ask user for starting chip amount
        self.total = int(input("How many chips do you want to start with? "))
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Functions for the game
def take_bet(chips):
    """  Step 6: Write a function for taking bets

    Since we're asking the user for an integer value, this would be a good place
    to use try/except. Remember to check that a Player's bet can be covered by
    their available chips.
    """
    while True:
        try:
            # Ask user for their bet
            chips.bet = int(input("How many chips do you want to bet? "))
        except ValueError:
            # User didnt enter an integer
            print("Sorry, a bet must be an integer!")
        else:
            # User entered an integer
            if chips.bet > chips.total:
                # User has tried to bet more than their chip total
                print("Sorry, your bet can't exceed", chips.total)
            else:
                # Bet amount has been set successfully
                break


def hit(deck, hand):
    """ Step 7: Write a function for taking hits

    Either player can take hits until they bust. This function will be called
    during gameplay anytime a Player requests a hit, or a Dealer's hand is less
    than 17. It should take in Deck and Hand objects as arguments, and deal one
    card off the deck and add it to the Hand. You may want it to check for aces
    in the event that a player's hand exceeds 21.
    """
    # Add a new card to the hand from the deck
    hand.add_card(deck.deal())
    # Check if needs to be adjusted for aces
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """ Step 8: Write a function prompting the Player to Hit or Stand

    This function should accept the deck and the player's hand as arguments,
    and assign playing as a global variable.

    If the Player Hits, employ the hit() function above. If the Player Stands,
    set the playing variable to False - this will control the behavior of a
    while loop later on in our code.
    """
    global playing  # to control an upcoming while loop

    # Ask user if they want to hit (pressing any key returns true)
    # or stand (pressing entering will return false)
    playing = bool(input("Do you want to hit (press any key) or stand (press enter)? "))

    if playing:
        # User wants to hit
        hit(deck, hand)


def show_hand(player, dealer):
    """   Step 9: Write functions to display cards

    When the game starts, and after each time Player takes a card, the dealer's
    first card is hidden and all of Player's cards are visible.

    At the end of the hand all cards are shown, and you may want to show each
    hand's total value. Write a function for each of these scenarios.
    """

    if playing:
        print("\nDealer's hand is:\n", dealer.cards[0], "\n  <HIDDEN>")
    else:
        print("\nDealer's total is", dealer.value, "and", dealer.__str__())

    print("\nPlayer's total is", player.value, "and", player.__str__())


def player_stands(player, dealer, chips):

    if player.value > 21:
        # If player's hand exceeds 21, run player_busts() and break out of loop
        print("Player busts!")
        chips.lose_bet()

    elif dealer.value > 21:
        # dealer_busts
        chips.win_bet()
        print("Dealer busts, Player wins")

    elif dealer.value > player.value:
        # dealer_wins
        chips.lose_bet()
        print("Dealer wins")

    elif dealer.value < player.value:
        chips.win_bet()
        print("Player wins")

    elif dealer.value == player.value:
        print("There has been a tie")


def starting_hand(deck):
    hand = Hand()
    hand.add_card(deck.deal())
    hand.add_card(deck.deal())
    return hand

def main():
    # Print an opening statement
    print("Let's play some Black Jack!")

    # Set up the Player's chips
    chips = Chips()
    round = 1

    while True:
        # Create & shuffle the deck,
        deck = Deck()
        deck.shuffle()
        # Deal two cards to each player
        player = starting_hand(deck)
        dealer = starting_hand(deck)
        # Prompt the Player for their bet
        take_bet(chips)

        # Show cards (but keep one dealer card hidden)
        print("-------------------------------------")
        print("STARTING HANDS! Round (", round, ")")
        show_hand(player, dealer)

        # Player starts
        count = 1
        while playing:
            print("-------------------------------------")
            print("PLAYER'S TURN (", count, ")")
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player)
            # Show cards (but keep one dealer card hidden)
            show_hand(player, dealer)
            count += 1

            # Check if player has bust
            if player.value > 21:
                break

        # If Player hasn't busted, it is Dealers turn
        if player.value < 21:
            # Play Dealer's hand until Dealer reaches 17
            while dealer.value < 17:
                hit(deck, dealer)

        # The game is over
        print("-------------------------------------")
        print("RESULT")
        # Show all cards
        show_hand(player, dealer)
        player_stands(player, dealer, chips)

        # Inform Player of their chips total
        print("-------------------------------------")
        print("Your chip total is: ", chips.total)

        # Ask to play again
        play_again = input("Do you want to play again? Yes (press any key) or No (press Enter)? ")
        if play_again:
            round += 1
            continue
        else:
            print("Thanks for playing!")
            break




if __name__ == "__main__":
    main()