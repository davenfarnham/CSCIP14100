#!/usr/bin/python

#
# An example program to test conditionals and cmd-line arguments
# Daven Farnham
# 2015
#

import sys

def check(c):
  if c < 4:
    print 'Rob sucks'
  elif c >= 5 and c < 10:
    print 'Ramon rocks'
  else:
    print 'Daven is awesome'

  return

def main():
  # good example of a conditional + CMD LINE arguments
  if len(sys.argv) < 2:
      print 'please give me an int!'
      return

  # change to int then pass to check()
  check(int(sys.argv[1]))

  return

if __name__ == '__main__':
  main()
