#!/usr/bin/python
import re

def sub(s):
  return re.sub(r'dumb', r'awesome', s)

def main():
  s = 'Daven is dumb'
  
  print sub(s)
  
if __name__=='__main__':
  main()