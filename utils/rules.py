import card_hand


class Rules:
    def __init__(self):
        self.winner = None

    # checks if player/dealer wins or if their is a draw
    def black_jack_check(self, player, dealer):
        if sum(dealer.cards) == 21:
            return False
        if sum(dealer.cards) == 21 and sum(player.cards) == 21:
            return None
        if sum(player.cards) == 21:
            return True

    # Checks if dealer or player is over 21
    def bust_check(self, player, dealer):
        if sum(player.cards) > 21:
            return False
        if sum(dealer.cards) > 21:
            return True

    # Checks if dealer is needs to draw
    def dealer_must_draw(self, dealer):
        while sum(dealer.cards) < 17:
            dealer.draw_additional_card

    # checks which hand  is higher than the other.
    def best_hand_check(self, player, dealer):
        if sum(player.cards) > sum(dealer.cards):
            return True
        elif sum(player.cards) == sum(dealer.cards):
            return None
        elif sum(player.cards) < sum(dealer.cards):
            return False
