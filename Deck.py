from Card import Card
# Import the random module to shuffle the deck prior to dealing.
import random

class Deck:
    """ A deck holds all cards and can be shuffled. All 52 unique card objects
    need to be initiated and added to a list.
    """

    def __init__(self):
        # Start with an empty list
        self.deck = []
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


        # Add each card to the list
        for suit in self.suits:
            for rank in self.ranks:
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
        # Use random to shuffle the deck
        random.shuffle(self.deck)

    def deal(self):
        # Remove the top card from the hand and return
        return self.deck.pop()