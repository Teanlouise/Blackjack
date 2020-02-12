from Hand import Hand

class Round:
    """ Each game has at least one round. During a round the dealer and player
    are dealt a hand and they take turns until a winner is found.
    """

    def __init__(self, game):
        self.game = game
        # Deal two cards to each player
        self.player = Hand(self)
        self.dealer = Hand(self)

    def show_hands(self):
        # Check if the player has had their turn
        if self.game.playing:
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
        print("--------------------------- ROUND", self.game.game_round, "---------------------------")
        # Prompt the Player for their bet
        self.game.chips.take_bet()

        # Show cards (but keep one dealer card hidden)
        print("\n___STARTING HANDS!___")
        self.show_hands()

        # Player starts
        turn = 1
        while self.game.playing:
            # Continue player's turn until STAND or BUST
            print("\n___PLAYER'S TURN (", turn, ")___")
            # Prompt for Player to Hit or Stand
            self.player.hit_or_stand()
            turn += 1

            # Check if player has bust
            if self.player.value > 21:
                # Break out of the loop and go to 'game over'
                self.game.playing = False

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