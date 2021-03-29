import random
import time

chip_amt = 0 # there is another one in the show_chip function ??
chip_bet = 0
dealer_card = [] # there is another one in the game_start function ??
player_card = [] # there is another one in the game_start function ??

chip_amt += int(input("How many chips do you want to buy? Integer Only: \n")) 
print("You now have {} chips. Let's play!".format(chip_amt))
time.sleep(1)

def show_chip():
# show and check the chip balance
    if chip_amt > 0:
        print("You now have {} chips.".format(chip_amt))
        chip_bet = 0
        user_input = input("Do you want to keep playing? Y/N \n")
        if user_input.upper() == "Y":
            pass

        else:
            print("You may exit the game by closing this window!")
            print("Your final balance is {}. Please contact cashier if you have balance.".format(chip_amt))
            # Q: how to exit the program when player choose to? 
    else:
        print("You are out of chips! Exiting the game!")

def player_blackjack_or_bust():
# check if the player cards sum is blackjack or bust
# Q: how to differentiate the dealer and the player?
    if sum(player_card) == 21:
        print("Blackjack! You WON!")
        chip_amt += chip_bet*2
        show_chip()
    elif sum(player_card) > 21:
        print("Busted! You Lost!")
        show_chip()
    else:
        pass


def game_start():

    global chip_amt
    global chip_bet

    while chip_amt > 0:
        #how to add another condition in which user_input is not N?

        chip_bet = int(input("How many chips do you want to bet this time? Integer Only: \n"))
        print("You have bet {} chips this round. Good Luck!". format(chip_bet))
        chip_amt -= chip_bet

        dealer_card = []
        player_card = []

        # dealer gets two cards and shows one of them
        while len(dealer_card) != 2:

            dealer_card.append(random.randint(1,11))
            if len(dealer_card) == 2:
                print("Dealer has two cards. One of them is:" + str(dealer_card[0]))

        # player gets two cards and shows both
        while len(player_card) != 2:

            player_card.append(random.randint(1,11))
            if len(player_card) == 2:
                print("Player 1 has two cards: ", player_card)
                if sum(player_card) > 21:
                    print("Busted! You Lost!")
                    show_chip()

        while sum(player_card) < 21:

            player_option = str(input("Choose one option: stop or hit?  \n"))
            if player_option.lower() == "hit":
                player_card.append(random.randint(1,11))
                print("You now have {}! ".format(player_card))
                player_blackjack_or_bust()

            else:
                print("You have stopped at {}! Dealer's move now!".format(sum(player_card)))
                player_blackjack_or_bust()
                break


        while sum(dealer_card) <= 16:

            dealer_card.append(random.randint(1,11))
            print("Dealer now have {}! ".format(dealer_card))
            time.sleep(1)
            if sum(dealer_card) > 16:
                break

        if sum(dealer_card) == 21 and sum(player_card) != 21:
            print("Dealer Blackjack! You Lost! Better luck next round!")
            show_chip()

        if sum(player_card) == 21 and sum(dealer_card) != 21:
            print("Blackjack! You WON!")
            chip_amt += chip_bet*2
            show_chip()

        if sum(dealer_card) > 21:
            print("Dealer Bust! You WON!")
            chip_amt += chip_bet*2
            show_chip()

        if sum(player_card) < 21 and sum(dealer_card) < 21:
            if sum(player_card) > sum(dealer_card):
                print("You have {} and dealer has {}.".format(sum(player_card),sum(dealer_card)))
                print("You WON! Congrats!")
                chip_amt += chip_bet*2
                show_chip()
            else:
                print("You have {} and dealer has {}.".format(sum(player_card),sum(dealer_card)))
                print("You Lost!")
                show_chip()
                continue        

game_start()                

# Q: Line 17, is it right to put it here?
# Q: How to indent when putting more time.sleep?
# Q: When to use return in function? how to set arguments in fuction?
