import random
import global_variables
from deck_class import Deck as Deck
from hand_class import Hand as Hand


# The Game is turned on
game_on = True

print("Create the new deck and print it out:")
test_deck = Deck()
print(test_deck)
print("\nShuffle it:")
test_deck.shuffle()
print(test_deck)

# TEST Player
test_player = Hand()
# Deal 1 card from the deck Card(suit, rank)
pulled_card = test_deck.deal()
print(f"\nThe pulled card is {pulled_card}")
test_player.add_card(pulled_card)
print(f"The value in the players hand is equal {test_player.value}")

