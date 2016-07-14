#!/usr/bin/python

# create a list. Lists are simply collections of things. They're denoted in brackets with separating commas
a = [1,2,3,4,5,6,7,8,9,10]

# define a count function
def count(b):

  # define a variable that you'll be updating as you sum up the ints in the list
  counter = 0

  # loop through list. Notice how this is different from what we did in class. Here, I'm passing the
  # count() function a variable, namely b. b is just a list of values, though. So, instead of doing:
  #
  #           for i in range (0, 6):
  #
  # I instead say,
  #
  #           for num in b:
  #
  # In the first iteration of this num == 1, then in the second iteration num == 2, continuing all the way
  # up until there are no more numbers in b.
  #
  # This kind of for-loop is a bit easier in case you don't know how many items are in the list, for example.
  #
  for num in b:
      counter = counter + num

  # return the value in counter here (be careful of indentation!)
  return counter

def main():
  # run your count function passing it an argument
  sum = count(a)

  # conditional
  if sum > 20:
    print 'You have: ' + str(sum) + '. Nice!'
  else:
    print 'lame'


if __name__ == '__main__':
    main()
