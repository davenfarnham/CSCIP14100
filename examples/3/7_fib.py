#!/usr/bin/python

def fib(n):
  if n <= 2: # if n == 1 or 2 return 1 since the 1st and 2nd Fibs are 1
    return 1
  else:
    return fib(n-1) + fib(n-2)

# 5 -> (fib(4) + fib(3)) -> (fib(3) + fib(2) | fib(2) + fib(1)) | (fib(2) + fib(1) | )
# 5    (  3    +    2  )    (  2    +     1) + (  1   +    1  )

def main():
  print fib(5)

if __name__=='__main__':
  main()
