#!/usr/bin/python

import re

def learning_dict():
  normal_d = {}

  # open dictionary
  f = open('small_dict.txt', 'r')
  words = f.read().split()

  # put into dictionary
  for word in words:
    normal_d[word.lower()] = None

  h = open('small_string.txt', 'r')

  # make a list of words from holy_grail.txt
  hg = h.read().split()

  # number of mispelled words
  count = 0

  incorrect_d = {}
  added = {}

  for l in hg:
    # add regular expression to deal with periods
    match = re.search(r'[\"]*(\w+)[\".!,?,/]*', l)
    if match:
      l = match.group(1)
    # turn all words in string to lower case to match dictionary
    if l.lower() not in normal_d:
      if l.lower() not in incorrect_d: 
        incorrect_d[l.lower()] = 1
        count = count + 1
      elif incorrect_d.get(l.lower()) == 1:
         incorrect_d[l.lower()] = 2
         count = count  + 1
      else:
        incorrect_d.pop(l.lower())
        count = count - 2
        normal_d[l.lower()] = None
        added[l.lower()] = None

  print added
  print incorrect_d
  print count


def main():
  learning_dict()

if __name__=='__main__':
  main()
