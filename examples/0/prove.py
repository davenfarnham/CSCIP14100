#!/usr/bin/python

# empty array
a = []

# create array from [1, n)
for i in range (1, 151):
  a.append(i)

# define a counter
def count(b):
  counter = 0

  # loop through list
  for num in b:
      counter = counter + num
  return counter

def main():
  # run your function
  print 'The sum is: ' + str(count(a))

if __name__ == '__main__':
    main()
