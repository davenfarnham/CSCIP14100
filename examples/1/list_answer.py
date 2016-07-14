#!/usr/bin/python

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  size = 0
  for word in words:
    if len(word) >= 2 and word[0].lower() == word[-1].lower():
      size = size + 1
  return size

def main():
  l = ['Mary', 'Anna', 'Mike', 'Miriam', 'Matt']

  print str(match_ends(l))

if __name__=='__main__':
  main()

