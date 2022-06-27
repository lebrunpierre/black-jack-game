import blackjack_actors
import rules
import blackjack_utils

# Game intro
print(blackjack_utils.black_jack_logo)
is_player_playing = input("Do you want to play a little game? \n Type 'y': ")

# Creating First Hand
player = blackjack_actors.blackJackActors("Player")
dealer = blackjack_actors.blackJackActors("Dealer")
player_draw = 'y'



while player_draw == 'y':
    # Checks to see if there is a winner. Assigned to variable to save space.
    check_rules_player_draw = rules.rule_check(player, dealer, False)
    check_rules_player_no_draw = rules.rule_check(player, dealer, True)

    player.show_cards()
    dealer.show_cards(True)
    # checks to see if there is any blackjack winners.
    if check_rules_player_draw is not None:
        dealer.final_outcome()
        print(check_rules_player_draw)
        break

    # Asks player if they want another card
    player_draw = input("Would you like to draw another card? \n" +
                       "Press 'y' for yes ")

    if player_draw == 'y':
        # draws card and checks dealer will draw if they need to.
        player.draw_additional_card()
        player.show_cards()
        rules.dealer_draw(dealer)

        # checks blackjack rules to see if there is a winner
        if check_rules_player_draw is not None:
            rules.dealer_draw(dealer)
            dealer.final_outcome()
            print(check_rules_player_draw)
            break
    else:
        # Player declines draw and rules are checked
        rules.dealer_draw(dealer)
        dealer.final_outcome()
        input()
        player.final_outcome()
        print(check_rules_player_no_draw)
