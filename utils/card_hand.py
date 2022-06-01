import random

import card_array


class CardHand:
    def __init__(self):
        self.cards = None
    # firs set of cards will be drawn
    def draw_cards(self):
        self.cards = [card_array.draw_card(), card_array.draw_card()]
    # if user or dealer needs to draw again
    def draw_additional_card(self):
        self.cards.append(card_array.draw_card())
    # shows dealers hand by not showing the first card
    def dealers_hand(self):
        print(self.cards[1:])
