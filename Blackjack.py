# 建立多玩家class，还不会弄
# class player:
#     def __init__(self, name, chips):
#         self.name = name
#         self.chips = chips
# Name = input("Please write down your name:" ) 
# Chips = input("Please write down the amount you would like to invest:")

import random
import time

dealer_card = []
player_card = []
chip_amt = 0  #初始筹码数量
chip_amt += int(input("How many chips do you want to buy? 整数: \n")) #下注
print("You now have {} chips. Let's play!".format(chip_amt))

time.sleep(1)

chip_bet = int(input("How many chips do you want to bet this time? 整数: \n"))
print("You have bet {} chips this round. Good Luck!". format(chip_bet))
chip_amt -= chip_bet

time.sleep(1)

def compare():
# 在玩家和庄家都没有bust和blackjack的情况下，比大小
    if sum(dealer_card) > sum(player_card):
        print("You have {}; Dealer has {}. \n You Lose! Better chance next time!".format(player_card, dealer_card))
        # print("You have {} chips left.".format(chip_amt))      
    elif sum(dealer_card) < sum(player_card):
        print("You have {}; Dealer has {}. \n YEAH! You WIN!!".format(player_card, dealer_card))
        # chip_amt += chip_bet * 2 
        # print("You now have {} chips left!".format(chip_amt))
    else:
        print("You have {}; Dealer has {}. \n Draw!!".format(player_card, dealer_card))
        # chip_amt += chip_bet

def dealer_move():
#在玩家结束它的操作后，庄家开始
    while sum(dealer_card) <= 16:
        print("Dealing...")
        dealer_card.append(random.randint(1,11))
        print("Dealer has {}".format(dealer_card))
        time.sleep(1)
        if 21 >= sum(dealer_card) > 17:
            print("Dealer stops at {}.".format(sum(dealer_card)))
            if sum(dealer_card) == 21:
                print("Dealer Blackjack! You Lose!")
            else:
                compare()

def bust_or_blackjack():
    while sum(player_card) < 21:
        player_option = str(input("Choose one option: stop or hit? 小写字母单词 \n"))
        if player_option == "hit":
            player_card.append(random.randint(1,11))
            print("You now have {}! ".format(player_card))
            if sum(player_card) > 21:
                print("Player Busted!")
                # print("You now have {} chips left!".format(chip_amt))
            if sum(player_card) == 21:
                print("Blackjack!! You WIN")
                # chip_amt += chip_bet * 2
                break               
        # elif sum(player_card) == 22: #在抽取两个数字都是11的情况下，玩家可以选择采用2或者12
        #     sum(player_card) = int(input("You could choose to have 2 or 12 points. Type In:\n"))
        #     bust_or_blackjack()
        else:
            dealer_move()

# 先发庄家，两张，一张显示，一张隐藏
while len(dealer_card) != 2:
    dealer_card.append(random.randint(1,11))
    if len(dealer_card) == 2:
        print("Dealer has two cards. One of them is:" + str(dealer_card[0]))

# 发牌玩家（如果多个玩家），每人2张，显示
while len(player_card) != 2:
    player_card.append(random.randint(1,11))
    if len(player_card) == 2:
        print("Player 1 has two cards: ", player_card)
        bust_or_blackjack()

# 几个小问题：
# 1. 如何在决胜之后，停止运行所有程序，从头开始？
# 2. 如果的输入的文字，大小写问题，怎么处理？
# 3. 如果筹码用完，怎么从头开始？
# 4. 软件提示我chip_amt这个变量有问题？
# 5. 按照规则，如果抽出的数字是11，可以当做1或者11，以有利于玩家为准，这个怎么操作？