#!/usr/bin/python

# A. string sort
# Given a list of strings, sort them based on their middle character. If a
# string has an even numbers of characters, sort by the (n/2 + 1) index.
# You can assume you won't be passed the empty string.

def helper(s):
  index = len(s) / 2
  return s[index]

def string_sort(words):
  updated = sorted(words, key=len)
  print sorted(updated, key=helper)

def main():
  l = ['aba', 'bab', 'crc', 'a', 'zz', 'f', 'aef', 'aazz']

  # just to check what the default it
  print sorted(l)

  string_sort(l)

if __name__=='__main__':
  main()

