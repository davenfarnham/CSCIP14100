#!/usr/bin/python

# recursive sum
def summ(n):
  if n == 1:
    return 1
  else:
    return n + summ(n-1)

def main():
  print summ(10)

if __name__=='__main__':
  main()