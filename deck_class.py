"""
In this file describes the Deck class
"""
import random
import global_variables
from card_class import Card as Card


class Deck:

    def __init__(self):
        self.deck = []      # Created once and don't change until the end of the game
        # Creation of the deck
        for suit in global_variables.suits:
            for rank in global_variables.ranks:
                self.deck.append(Card(suit, rank))

# In this way we created the new deck full of 52 objects belongs to the Card class

    def __str__(self):
        # we're using the string for representation of our new one deck
        deck_composition = ""
        for card in self.deck:
            deck_composition += "\n" + card.__str__()
        return "The deck has: " + deck_composition

    def shuffle(self):
        # need for shuffle action
        random.shuffle(self.deck)       # do not need to use return, because shuffle method shuffling the list in place

    def deal(self):
        single_card = self.deck.pop()
        return single_card

