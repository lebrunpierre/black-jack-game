import card_hand
class Rules:
    def __init__(self):
        self.winner = None

    def black_jack_check(self, player, dealer):
        if sum(dealer.cards) == 21:
            return False
        if sum(player.cards) == 21:
            return True

    def bust_check(self, player, dealer):
        if sum(player.cards) > 21:
            return False
        if sum(dealer.cards) > 21:
            return True

    def dealer_must_draw(self, dealer):
        while sum(dealer.cards) < 17:
            dealer.draw_additional_card

    def best_hand_check(self, player, dealer):
            if sum(player.cards) > sum(dealer.cards):
                return True
            else:
                return False
