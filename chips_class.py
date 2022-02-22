"""
In this file will I will describe the chips class
"""


class Chips:
    def __init__(self, total=1000):      # default value of chips is 100
        self.total = total      # here we can set value for he default or let a user input a num
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

