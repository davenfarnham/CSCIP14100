#!/usr/bin/python
import re

# match on c3p0's name
def star_wars():
  s = '     hi      there  c3p0!  How are you'

  # direct search
  match = re.search(r'c3p0', s)

  print match.group()

  # search on a pattern
  match = re.search(r'\w\d\w\d', s)

  print match.group()

def main():
  star_wars()

if __name__=='__main__':
  main()
