#!/usr/bin/python 

def ho(f, x):

  for i in range (len(x)):
    x[i] = f(x[i])

  return x

def main():

  f = lambda x: x * 3

  l = [1, 2, 3, 4]

  print ho(f, l)

if __name__=='__main__':
  main()