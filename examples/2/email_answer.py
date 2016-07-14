#!/usr/bin/python
import re

# find the email address out of a string using a pattern
def email(s):
  # search on a pattern
  match = re.search(r'\w+@\w+[.]\w+', s)

  print match.group()

def main():
  s = ' hey! My email is daven@cs50.net. Hit me up!'

  email(s)

if __name__=='__main__':
  main()
