#!/usr/bin/python
import re

# find the email address out of a string using a pattern
def email(s):
  # search on a pattern. Let's say I don't want the entire emails but just the
  # names - then I can add () to just selectively pull out the names
  matches = re.findall(r'\w+@\w+[.]\w+[.]*\w*', s)
  
  for match in matches:
    print match
    
def main():
  s = 'Their emails are rob@cs.harvard.edu, gabe@cs50.net, and malan@harvard.edu'
  
  email(s)
  
if __name__=='__main__':
  main()