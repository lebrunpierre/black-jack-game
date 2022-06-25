import random

import blackjack_utils


class CardHand:
    def __init__(self):
        self.cards = None

    # first set of cards will be drawn
    def draw_cards(self):
        self.cards = [blackjack_utils.draw_card(), blackjack_utils.draw_card()]

    # if user or dealer needs to draw again
    def draw_additional_card(self):
        self.cards.append(blackjack_utils.draw_card())

    # shows dealers hand by not showing the first card
    def dealers_hand(self):
        print(self.cards[1:])
