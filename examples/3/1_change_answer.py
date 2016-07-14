#!/usr/bin/python
import re

def change():
  f = open('grades.txt', 'r')
  
  grades = f.read()
  
  grades = re.sub(r'[CDF]\n', r'A\n', grades) 

  f.close()

  return grades

def main():
  updated = change()
  
  print updated
  
if __name__=='__main__':
  main()