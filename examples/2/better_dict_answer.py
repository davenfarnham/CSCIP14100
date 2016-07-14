#!/usr/bin/python

# A. use_dict
# Given a small dictionary in list form, convert to dict in use_dict()
import re

def create_dict():

  d = {}

  # open dictionary
  f = open('words.txt', 'r')
  words = f.read().split()
  
  # put into dictionary
  for word in words:
    d[word.lower()] = None
   
  # return dictionary 
  return d

def use_dict(s, d):
  # split string based on whitespace
  lst = s.split()
  
  # number of mispelled words
  count = 0
  
  for l in lst:
    # add regular expression to deal with periods
    if re.search(r'[.!,?]$',l):
      l = l[:-1]
    # turn all words in string to lower case to match dictionary
    if l.lower() not in d:
      print l
      count = count  + 1
  
  return count
  
def main():
    
  dic = create_dict()  
  string = 'This is a test string. All the words should be in the dictionary.'
  email = 'Both of the questions in monty.py are a little difficult, but somewhat iconic in CS. If you have questions on any of the parts we can definitely talk about them later this morning!'
  
  errors = use_dict(string, dic)
  errors = errors + use_dict(email, dic)
  
  if errors:
    print str(errors)
  else:
    print 'Nice! No mispellings! Well done!'
    
  return
  
if __name__=='__main__':
  main()