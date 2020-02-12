class Hand:
    """ A hand holds the cards that have been dealt to a player from the deck.
    It also calculates the value of the those cards and adjusts for aces when
    appropriate.

    """
    def __init__(self, round):
        self.cards = []  # start with an empty list
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

        self.round = round
        self.game = round.game
        self.deck = self.game.deck

        self.add_card(self.deck.deal())
        self.add_card(self.deck.deal())

    def add_card(self, card):
        # Add a card to the hand
        self.cards.append(card)
        # Add new cards value, according to rank, to the hand sum
        self.value += self.deck.values[card.rank]

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

    def hit_or_stand(self):
        # Ask user if they want to hit (pressing any key returns true)
        # or stand (pressing entering will return false)
        self.game.playing = bool(input(
            "Do you want to hit (press any key) or stand (press enter)? "))

        if self.game.playing:
            # User wants to hit
            self.hit()
            if self.value <= 21:
                # Show cards (but keep one dealer card hidden)
                self.round.show_hands()

    def __str__(self):
        # start with an empty string
        hand_str = ''
        # start with an empty string
        for card in self.cards:
            hand_str += '\n  '+ card.__str__()
        return 'hand is:' + hand_str