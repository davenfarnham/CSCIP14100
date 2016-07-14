#!/usr/bin/python

#
# Question 0
#
# You remember yesterday how we wrote that little program, I think we called
# it count. Basically what it did was declare a list of natural numbers then
# summed them from 1 to n.
#
# So, for example, if we hardcoded the list [1,2,3,4,5] and then called
# count(), we get back 15.
#
# Well, hardcoding values like the above isn't cool. For Question 1, take in
# a value from the user via the command line (by using argv) making sure to
# check the length of argv. Then generate a list of n numbers. Each number, though,
# should be ODD (so the list will look like [1, 3, 5, 7, ..., n]).
#
# Dynamically generate this list, perhaps using something like the append function we used
# today, and then sum up all the terms in the list. You should find that your sum == n^2.
#
# For this problem you should write a function, square(n) that will (1) generate the list
# of numbers and (2) sum them up. You should, as well, make your own main() function, as this
# will be what passes the cmd-line argument back to square(n)
#
# Your program should function from the cmd line like this:
#
#               ./square [nothing]         # prints error message
#               ./square 2                 # 4
#               ./square 3                 # 9
#               ./square 25                # 625
#
#

def square(n):
    # TODO

def main():
    # TODO

if __name__:'__main__':
    main()
