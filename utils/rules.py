import blackjack_actors

win = ' Player won'
lose = 'Player lost'
draw = "Draw no winner"


# checks if player/dealer wins or if their is a draw
def black_jack_check(player, dealer):
    if dealer.get_total() == 21 and player.get_total == 21:
        return draw
    if dealer.get_total() == 21:
        return lose
    if player.get_total() == 21:
        return win
    else:
        return None


# Checks if dealer or player is over 21
def bust_check(player, dealer):
    if sum(player.cards) > 21:
        return lose
    if sum(dealer.cards) > 21:
        return win
    else:
        return None


# Checks if dealer is needs to draw
def dealer_draw(player, dealer):
    while sum(dealer.cards) < 16:
        dealer.draw_additional_card()
        print("Dealer cards are under 17. Dealer Hits")
        input()
        dealer.show_cards(True)
        input()
    if sum(dealer.cards) >= 17:
        print("Dealer stands.")
        input()


# checks which hand  is higher than the other.
def best_hand_check(player, dealer):
    if sum(player.cards) > sum(dealer.cards):
        return win
    elif sum(player.cards) == sum(dealer.cards):
        return draw
    elif sum(player.cards) < sum(dealer.cards):
        return lose


def rule_check(player, dealer, is_final_hand=False):
    if black_jack_check(player, dealer) is not None:
        return black_jack_check(player, dealer)

    elif bust_check(player, dealer) is not None:
        return bust_check(player, dealer)

    elif is_final_hand is True:
        return best_hand_check(player, dealer)
