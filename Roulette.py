import random
import time
from sys import exit
red = [1, 3, 5, 7, 9, 12,
14, 16, 18, 19, 21, 23,
25, 27, 30, 32, 34, 36]

black = [2, 4, 6, 8, 10, 11,
13, 15, 17, 20, 22, 24,
26, 28, 29, 31, 33, 35]

def playerBet(money):
    more = True
    bets = []
    while more:
        rb = raw_input('1.Red\n2.Black\n3.Even\n4.Odd\n5.Single Number\n')
        rb = int(rb)
        while rb<1 or rb>5:
            rb = raw_input('1.Red\n2.Black\n3.Even\n4.Odd\n5.Single Number\n')
            rb = int(rb)
        if rb==5:
            num = raw_input('Number to bet on: ')
            num = int(num)
            while num < 1 or num > 36:
                num = raw_input('Number to bet on: ')
                num = int(num)
            rb = [5,num]
        ins = raw_input('Make a bet: ')
        ins = int(ins)
        while ins < 1 or ins > money:
            ins = raw_input('Invalid bet. Bet Again: ')
            ins = int(ins)
        money -= ins
        print money
        bet = [rb,ins]
        bets.append(bet)

        more = raw_input('Bet again?: ')
        more.lower()
        while more != 'y' and more !='yes' and more !='n' and more!='no':
            more = raw_input('Bet again?: ')
            more.lower()
        if more=='y' or more=='yes':
            more= True
        else:
            more=False
    return bets
    
def roulette():
    print "The winning number is..."
    win = random.randint(1,36)
    time.sleep(2)
    print win
    return win

def winnings(bets, win):
    winning_money = 0
    for bet in bets:
        if bet[0] is list > 1:
            s = bet[0]
            t = s[1]
            if win == t:
                print 'win'
                winning_money += bet[1] *36
        else:
            if win in red and bet[0] == 1:
                print 'win'
                winning_money += bet[1] * 2
            elif win in black and bet[0] == 2:
                print 'win'
                winning_money += bet[1] *2
            elif bet[0] == 3 and win%2==0:
                print 'win'
                winning_money +=bet[1] * 3
            elif bet[0] == 4 and win%2!=0:
                print 'win'
                winning_money +=bet[1] * 3
            else:
                print 'lose'
    return winning_money

#Start of main
money = raw_input('How much money do you want?: ')
money = int(money)
while money < 1:
    money = raw_input('How much money do you want?: ')
    money = int(money)
play = True
while play:
    bets = playerBet(money)
    for bet in bets:
        money = money - bet[1]
    win = roulette()
    money += winnings(bets,win)
    if money==0:
        print "You have no more money. You don't have to go home, but you can't stay here."
        exit(0)
    else:
        again = raw_input('You have %d. Would you like to play again?: ' %money)
        again.lower()
        while again != 'y' and again!='yes' and again!='n' and again!='no':
            raw_input('You have %d. Would you like to play again?: ' %money)
        if again == 'y' or again =='yes':
            play = True
        else:
            play = False

