import blackjack_actors
import rules
import blackjack_utils

# Game intro
print(blackjack_utils.black_jack_logo)
is_player_playing = input("Do you want to play a little game? \n Type 'y': ")

# Creating First Hand
player = blackjack_actors.blackJackActors("Player")
dealer = blackjack_actors.blackJackActors("Dealer")
player_hit = 'y'
player.show_cards()
dealer.show_cards(True)

while player_hit == 'y':
    # checks to see if there is any blackjack winners.
    if rules.rule_check(player, dealer, False) is not None:
        print(rules.rule_check(player, dealer, False))
        break

    # Asks player if they want another card
    player_hit = input("Would you like to draw another card? \n" +
                       "Press 'y' for yes ")

    if player_hit == 'y':
        # draws card and checks dealer will hit if they need to.
        player.draw_additional_card()
        player.show_cards()
        rules.dealer_draw(dealer)

        # checks blackjack rules to see if there is a winner
        if rules.rule_check(player, dealer, False) is not None:
            print(rules.rule_check(player, dealer, False))
            dealer.get_total()
            break
    else:
        # Player declines hit and rules are checked
        dealer.final_outcome()
        input()
        player.final_outcome()
        print(rules.rule_check(player, dealer, True))
