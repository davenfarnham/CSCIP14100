#!/usr/bin/python


def find(s, n, c):
  # recursive
  if n < 1: 
    print 'Not Found!'
  elif s[n-1] == c:
    print 'Found!'
  else:
    find(s, n-1, c)

  # iterative
  for i in range(0, len(s)):
    if s[i] == c:
      print 'Found!'
      return 
  
  print 'Not Found!'
  return

def main():
  find('kevin', 5, 'v')
  
if __name__=='__main__':
  main()