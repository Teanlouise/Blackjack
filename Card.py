class Card:
    """ A card has a suit and a rank."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # String in the format "RANK of SUIT"
        return self.rank + ' of ' + self.suit