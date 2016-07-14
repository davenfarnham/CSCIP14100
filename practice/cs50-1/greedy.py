#!/usr/bin/env python

# import library
import sys

#define values
quarter = .25
dime = .10
nickel = .05

# have a helper function cause why not
def change(change):
    # set initial value for coins
    coins = 0

    # check if change is greater than a quarter
    if(change >= quarter):
        # increment quarters
        coins = change // quarter
        # update the amount of change left
        change = change - ((change // quarter) * quarter)

    # repeat above algorithm
    if(change >= dime):
        coins = coins + change // dime
        change = change - ((change // dime) * dime)

    if(change >= nickel):
        coins = coins + change // nickel
        change = change - ((change // nickel) * nickel)

    # add on the pennies
    coins = coins + (change * 100)

    return coins

def main():
    # check length of cmd-line input
    if(len(sys.argv) < 2):
        print 'Give me an int!'
    else:
        # print the return of function change(); take the float value of argv[1] then round it (in case # of decimal places > 2)
        print change(round(float(sys.argv[1]), 2))

if __name__ == '__main__':
    main()
