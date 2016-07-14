#!/usr/bin/python

#
# Don't just print 'hello world' but add a name
# Daven Farnham
# 2015
#

import sys

def hello_world():
    if len(sys.argv) < 2:
      print 'add a name!'
    else:
      print 'hi ' + sys.argv[1] + '!'

def main():
    hello_world()

# used by the python interpreter to figure out which program in the 'main' one
if __name__ == '__main__':
    main() # execute this function
