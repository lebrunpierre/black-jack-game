import card_hand
import blackjack_utils
print(blackjack_utils.black_jack_logo)
p1 = card_hand.CardHand()
p1.draw_cards()
print(p1.dealers_hand())
