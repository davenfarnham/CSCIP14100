#!/usr/bin/python

import re

def main():
  # string of names
  names = 'marissa shay kevin alex sabrina will brenda holden'
  
  # split into list
  n = names.split()
  
  # use HO function filter
  name = filter(lambda x: re.search(r'^\w{6}$|^\w{4}$', x), n)
  
  s = ''
  
  # put names back together
  for i in range(len(name)):
    if i == len(name) - 1:
      s = s + name[i]
    else:
      s = s + name[i] + ' '
  
  print s
  
if __name__=='__main__':
  main()