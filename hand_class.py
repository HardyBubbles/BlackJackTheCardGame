"""
The Hand class is going to represent what cards are currently in someone's hand
"""
import global_variables
from card_class import Card as Card
from deck_class import Deck as Deck


class Hand:
    def __init__(self):
        self.cards = []     # start with an empty list
        self.value = 0      # at the start of the game and empty hand value is equal to 0
        self.aces = 0       # special attribute to keep track of aces

    def add_card(self, card):
        # card passed in from Deck.deal() --> single Card(suit, rank)
        self.cards.append(card)
        # Increase the self.value by value of took card
        self.value += global_variables.values[card.rank]

        # track aces
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        # If total value > 21 and I still have an ace, than change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

