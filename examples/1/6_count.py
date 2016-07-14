#!/usr/bin/python
import sys

# define a count function
def count(b):

  # define a variable that you'll be updating as you sum up the ints in the list
  counter = 0

  a = []

  # create an array of numbers
  for i in range(0, b + 1):
    a.append(i)

 # add the numbers up
  for num in a:
      counter = counter + num

  # return the value in counter here (be careful of indentation!)
  return counter

def main():

  if len(sys.argv) < 2:
    print 'please give me a number!'
  else:
    print 'The sum of ' + (sys.argv[1]) + ' numbers is: ' + str(count(int(sys.argv[1])))

if __name__ == '__main__':
    main()
