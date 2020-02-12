import pytest

from Card import Card
from Deck import Deck
from Game import Game
from Round import Round
from Hand import Hand
from Chips import Chips


deck_ordered = """
Two of Hearts
Three of Hearts
Four of Hearts
Five of Hearts
Six of Hearts
Seven of Hearts
Eight of Hearts
Nine of Hearts
Ten of Hearts
Jack of Hearts
Queen of Hearts
King of Hearts
Ace of Hearts
Two of Diamonds
Three of Diamonds
Four of Diamonds
Five of Diamonds
Six of Diamonds
Seven of Diamonds
Eight of Diamonds
Nine of Diamonds
Ten of Diamonds
Jack of Diamonds
Queen of Diamonds
King of Diamonds
Ace of Diamonds
Two of Spades
Three of Spades
Four of Spades
Five of Spades
Six of Spades
Seven of Spades
Eight of Spades
Nine of Spades
Ten of Spades
Jack of Spades
Queen of Spades
King of Spades
Ace of Spades
Two of Clubs
Three of Clubs
Four of Clubs
Five of Clubs
Six of Clubs
Seven of Clubs
Eight of Clubs
Nine of Clubs
Ten of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs
Ace of Clubs"""


# CARD
def test_card_string():
    card = Card('Hearts', 'Two')
    assert card.__str__() == "Two of Hearts"


# DECK
def test_deck_deal():
    deck_ordered = Deck()
    # Check before shuffled
    pop = deck_ordered.deal()
    assert pop.__str__() == 'Ace of Clubs'


def test_deck_shuffle():
    deck = Deck()

    # Check before shuffled
    assert deck.__str__() == deck_ordered

    # Check after shuffled
    deck.shuffle()
    assert deck.__str__() != deck_ordered


# CHIPS
def test_chips_balance_true():
    chips = Chips()
    chips.total = 100
    # There are chips, return true
    assert chips.check_balance()


def test_chips_balance_false():
    chips = Chips()
    assert not chips.check_balance()
    # There are no chips
    chips.total = 100
    chips.bet = 100
    chips.lose_bet()
    assert not chips.check_balance()


# ROUND
def test_player_busts():
    game = Game()
    round = Round(game)
    chips = game.chips
    chips.total = 100
    chips.bet = 10

    # Setup player to bust
    round.player.value = 22
    round.get_the_winner()  # chips.lose_bet
    assert chips.total == 90


def test_dealer_busts():
    game = Game()
    round = Round(game)
    chips = game.chips
    chips.total = 100
    chips.bet = 10

    # Setup dealer to bust
    round.dealer.value = 22
    round.get_the_winner()  # chips.win_bet
    assert chips.total == 110


def test_dealer_wins():
    game = Game()
    round = Round(game)
    chips = game.chips
    chips.total = 100
    chips.bet = 10

    # Setup dealer to win
    round.player.value = 19
    round.dealer.value = 20
    round.get_the_winner()  # chips.lose_bet
    assert chips.total == 90


def test_player_wins():
    game = Game()
    round = Round(game)
    chips = game.chips
    chips.total = 100
    chips.bet = 10

    # Setup player to win
    round.player.value = 20
    round.dealer.value = 19
    round.get_the_winner()  # chips.win_bet
    assert chips.total == 110


def test_tie():
    game = Game()
    round = Round(game)
    chips = game.chips
    chips.total = 100
    chips.bet = 10

    # Setup tie
    round.player.value = 20
    round.dealer.value = 20
    round.get_the_winner()
    assert chips.total == 100


# HAND
# def test_hand_adjust_for_ace():
# def test_hand_hit():
# def test_hand_hit_or_stand():
def test_hand_add_card():
    game = Game()
    round = Round(game)
    card = Card('Hearts', 'Two')
    round.player.add_card(card)
    assert round.player.__str__() == "hand is:\n  Two of Hearts"


# GAME
# def test_game_play_game():
# def test_round_show_hands():
# def test_round_play_round():
