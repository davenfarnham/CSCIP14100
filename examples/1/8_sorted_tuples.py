#!/usr/bin/python

#
# Sort based on the second term in a tuple
# Daven Farnham
# 2015
#

# sort based on the second term inthe tuple
def tup(t):
  l, r = t # pattern match on the tuple
  return r


def main():
  # example array to check
  tups = [(2, 1), (0, 4), (8, -1)]

  # check with normal sort function
  print sorted(tups)

  # custom sort function
  print sorted(tups, key = tup) # pass in a custom function (can take only one argument)

if __name__=='__main__':
  main()
