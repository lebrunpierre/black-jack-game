import random

import blackjack_utils


class blackJackActors:
    """
    Creates player objects. keeps track of cards and name along with other functions.
    """
    def __init__(self, name):
        self.cards = [blackjack_utils.draw_card(), blackjack_utils.draw_card()]
        self.name = name

    def get_total(self):
        """
        Gets the total for actor cards
        :return:
        """
        return sum(self.cards)

    # if user or dealer needs to draw again
    def draw_additional_card(self):
        """
        Used for interactive card drawing
        :return:
        """
        self.cards.append(blackjack_utils.draw_card())

    # shows dealers hand by not showing the first card
    def show_cards(self, hide_first_card=False):
        """
        Print statements used to update user on actors cards.
        :param hide_first_card: used to show if first card needs to be hidden. (for dealer use)
        :return:
        """
        if hide_first_card:
            print(f"{self.name}: {self.cards[1:]}")
        else:
            print(f"{self.name}: {self.cards} total is {self.get_total()}")

    def final_outcome(self):
        """
        Prints thed final total for actor along with a basic statment
        :return:
        """
        print(f"{self.name} card total: {self.cards} = {self.get_total()}")
