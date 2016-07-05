import sys
import random
import math

def main():
    print("Hello there. Welcome to the ZCasino roulette! \n")
    sold = input("How much money do you have? \n")
    while sold > 0:
        print "The roulette is about to spin... Your sold: %d$" % sold
        bet = input("How much would you like to bet? \n")
        sold -= bet
        while true:
            try:
                player_number = input("On which number? (Please enter a number between 0 and 49) \n")
                assert player_number >= 0 and player_number < 50
                break
            except AssertionError:
                print "Sorry the number you entered must be between 0 and 49"
        ball_number = random.randrange(50)
        if player_number == ball_number:
            gain = 3 * bet
            sold += bet + gain
            print "Yay! Nice bet, you won: %d$" % gain
        elif player_number % 2 == ball_number % 2:
            gain = math.ceil(bet / 2)
            sold += bet + gain
            print "Hm... Almost. You can only have: %d$" % gain
        else:
            print "Sorry pal, you lost your bet"
    if sold == 0:
        print "Looks like you used all your money...\nThanks for playing!"

            
# Calls main
if __name__ == '__main__':
    main()