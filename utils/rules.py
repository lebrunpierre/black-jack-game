import blackjack_actors

# used to print out the results to the user.
win = ' Player won'
lose = 'Player lost'
draw = "Draw no winner"


# checks if player/dealer wins or if there is a draw
def black_jack_check(player, dealer):
    """
    Checks to see if actor or dealer has blackjack
    :param player:
    :param dealer:
    :return:
    """
    if dealer.get_total() == 21 and player.get_total == 21:
        return draw
    elif dealer.get_total() == 21:
        return lose
    elif player.get_total() == 21:
        return win
    else:
        return None


# Checks if dealer or player is over 21
def bust_check(player, dealer):
    """
    Checks if player or dealer has gone over 21 in card totall
    :param player:
    :param dealer:
    :return:
    """
    if player.get_total() > 21 and dealer.get_total() > 21:
        return draw
    elif player.get_total() > 21:
        return lose
    elif dealer.get_total() > 21:
        return win
    else:
        return None


# Checks if dealer is needs to draw
def dealer_draw(dealer):
    """
    Checks if dealer needs to draw.
    If dealer cards are less than 16 dealer will keep drawing.
    Dealer will stand at 17
    :param dealer:
    :return:
    """
    while sum(dealer.cards) <= 16:
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
    """
    If user chooses to not hit. This method will be used to see who is the closer to 21
    :param player:
    :param dealer:
    :return:
    """
    if sum(dealer.cards) < sum(player.cards) and sum(player.cards) < 21:
        return win
    elif sum(dealer.cards) == sum(player.cards) and sum(dealer.cards) < 21:
        return draw
    elif sum(dealer.cards) > sum(player.cards) and sum(dealer.cards) < 21:
        return lose


def rule_check(player, dealer, is_final_hand=False):
    """
    Checks all the rules to avoid writing out the above function multiple times.
    :param player:
    :param dealer:
    :param is_final_hand: used to flag if user is not going to draw another card.
    :return:
    """

    if bust_check(player, dealer) is not None:
        return bust_check(player, dealer)

    elif is_final_hand:
        return best_hand_check(player, dealer)

    elif black_jack_check(player, dealer) is not None:
        return black_jack_check(player, dealer)



