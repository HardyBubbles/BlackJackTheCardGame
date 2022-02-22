"""
Here will describe functions for the game
"""


# Function for make a bet
def take_bet(chips):

    while True:
        # Use exception for checking input is integer or not
        try:
            chips.bet = int(input("Please input how many chips would you like to bet: "))
        except:     # type(chips.bet) != type(2)
            print("Sorry, please provide the integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break


# Function for take a hit
def hit(deck, hand):
    hand.add_card(deck.deal())
    # Do not forget about adjust_for_aces method
    hand.adjust_for_ace()


# Function for asking the player to hit or stand
def hit_or_stand(deck, hand):
    global game_on      # to control an upcoming while loop

    while True:
        answer = input("Hit or Stand? Enter h or s: ").lower()

        if answer[0] == "h":     # we're grab the first one letter of the answer
            hit(deck, hand)      # hit function defined above
        elif answer[0] == "s":
            print("Player Stands - Dealer's Turn")
            game_on = False
        else:
            print("Sorry , I did no understand that, please enter h or s letter only!")
            continue
        break


# Functions for display cards
def show_some(player, dealer):

    # Show only ONE card of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])      # Display only the second card

    # Show all (2 cards) of the player's hand/cards
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):

    # Show all dealer's cards
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    # Calculate and display value
    print(f"Value of Dealer's hand is: {dealer.value}")

    # Show all player's cards
    print("\n Player's hand: ", *player.cards, sep="\n")
    # Calculate and display value
    print(f"Value of Dealer's hand is: {player.value}")


# Functions to handle end of game scenarios
def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! PUSH")

