import blackjack_actors
import rules
import blackjack_utils

# Creating First Hand
print(blackjack_utils.black_jack_logo)
is_player_playing = input("Do you want to play a little game? \n Type 'y': ")

player = blackjack_actors.CardHand("Player")
dealer = blackjack_actors.CardHand("Dealer")
player_hit = 'y'
player.show_cards()
dealer.show_cards(True)


while player_hit == 'y':
    if rules.rule_check(player, dealer, False) != None:
        print(rules.rule_check(player, dealer, False))
        break
    player_hit = input("Would you like to draw another card? \n" +
                       "Press 'y' for yes ")
    if player_hit == 'y':
        player.draw_additional_card()
        player.show_cards()
        rules.dealer_draw(player, dealer)

        if rules.rule_check(player, dealer, False) != None:
            print(rules.rule_check(player, dealer, False))
            dealer.get_total()
            break
    else:
        dealer.final_outcome()
        input()
        player.final_outcome()
        print(rules.rule_check(player, dealer, True))


