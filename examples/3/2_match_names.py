#!/usr/bin/python

import re

def main():
  # have a string with students
  names = 'marissa, shay, kevin, alex, sabrina, will, brenda, holden.'
  
  # use both the number of characters & or operator
  match = re.findall(r'\s\w{6}[,.]|\s\w{4}[,.]', names)
  
  # print out the list
  print match
  
if __name__=='__main__':
  main()