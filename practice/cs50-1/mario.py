#!/usr/bin/env python

# 
# CS50's pset 1 mario.c, from 'C', in Python
# Daven Farnham June 3rd, 2015
#

# import system module
import sys

# define a main function
def main():
    # check number of cmd-line arguments
    if(len(sys.argv) < 2):
        print 'Please give me a number >= 0 or <= 24!'
        return

    # size of pyramid
    size = int(sys.argv[1])

    # check and make sure user input is [0, 24)
    while(size < 0 or size >= 24):
        # prompt user for input
        size = input('Please give me a number >= 0 or <= 24!: ')
        size = int(size)

    # logic behind printing out pyramid
    length = size
    while(length >= 1):
        for i in range (1, length):
            sys.stdout.write(' ')
        for k in range (length - 1, size):
            sys.stdout.write('#')
        # print out newline
        print ''
        # decrement length
        length = length - 1

# run main function
if __name__ == '__main__':
    main()
