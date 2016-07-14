#!/usr/bin/python

# A. use_dict
# Given a small dictionary of only lower case words in list form,
# convert to dict in use_dict()
def create_dict():

  d = {}

  # open dictionary
  f = open('words.txt', 'r')
  # reand into words the dictionary, splitting based on whitespace
  words = f.read().split()

  for word in words:
    d[word.lower()] = None

  return d

# pass into use_dict the string you're checking, s, and the dictionary, d
def use_dict(s, d):
  # split string s based on whitespace
  lst = s.split()

  # number of mispelled words
  count = 0

  for a in lst:
    if a.lower() not in d:
      count = count + 1
      print a.lower()

  return count

def main():

  # call your create_dict function
  dic = create_dict()

  # sample strings
  string = 'This is a test string All the words should be in the dictionary'

  email = 'Both of the questions in monty.py are a little difficult, but somewhat iconic in CS. If you have questions on any of the parts we can definitely talk about them later this morning!'

  # count # of mispelling words
  errors = use_dict(string, dic)
  errors = errors + use_dict(email, dic)

  # if errors, print out how many
  if errors:
    print str(errors)
  # else congratulate user
  else:
    print 'Nice! No mispellings! Well done!'

  return

if __name__=='__main__':
  main()
