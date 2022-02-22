import functions
from deck_class import Deck as Deck
from hand_class import Hand as Hand
from chips_class import Chips as Chips


# The Game is turned on
game_on = True


# GAME LOGIC
while game_on:

    print("Welcome to BlackJack")
    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    for i in range(2):
        player_hand.add_card(deck.deal())
        i += 1

    dealer_hand = Hand()
    for i in range(2):
        dealer_hand.add_card(deck.deal())
        i += 1

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Players for their bet
    functions.take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    functions.show_some(player_hand, dealer_hand)

    while game_on:     # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        functions.hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer hidden)
        functions.show_some(player_hand, dealer_hand)

        # If Player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            functions.player_busts(player_hand, dealer_hand, player_chips)

        break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 - usually used limit for casino
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            functions.hit(deck, dealer_hand)

        # Show all cards
        functions.show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            functions.dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            functions.dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            functions.player_wins(player_hand, dealer_hand, player_chips)
        else:
            functions.push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f"\n Player's total chips are at: {player_chips.total}")

    # Ask to play again
    new_game = input("Would you like to play again? Please input Y or N: ").lower()

    if new_game[0] == "y":
        game_on = True
        continue
    else:
        print("Thank you for playing!")
        break
