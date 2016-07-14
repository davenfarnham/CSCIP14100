#!/usr/bin/python
import re

def change():
  f = open('grades.txt', 'r')
  
  grades = f.read()
  
  grades = re.sub(r' C', r' A' , grades) 

  return grades

def main():
  updated = change()
  
  print updated
  
if __name__=='__main__':
  main()