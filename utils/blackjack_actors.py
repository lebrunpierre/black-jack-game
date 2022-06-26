import random

import blackjack_utils


class CardHand:
    def __init__(self, name):
        self.cards = [blackjack_utils.draw_card(), blackjack_utils.draw_card()]
        self.name = name

    def get_total(self):
        return sum(self.cards)

    # if user or dealer needs to draw again
    def draw_additional_card(self):
        self.cards.append(blackjack_utils.draw_card())

    # shows dealers hand by not showing the first card
    def show_cards(self, hide_first_card=False):
        if hide_first_card:
            print(f"{self.name}: {self.cards[1:]}")
        else:
            print(f"{self.name}: {self.cards} total is {self.get_total()}")

    def final_outcome(self):
        print(f"{self.name} card total: {self.cards} = {self.get_total()}")
