class Chips:
    """Keeps track of a Player's starting chips, bets and ongoing winnings."""

    def __init__(self):
        # Ask user for starting chip amount
        self.total = 0
        self.bet = 0

    def ask_chips(self):
        self.total = int(input("How many chips do you want to start with? "))

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