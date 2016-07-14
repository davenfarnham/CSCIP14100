#!/usr/bin/python

# run length encoding for compression
def run_length(l):
  # empty list
  tups = []

  # counter for while
  i = 0

  # iterate over list
  while i < len(l):
    # whatever the current number is
    current = l[i]
    # count for how many times the current number has appeared
    count = 1

    # iterate down the list, checking if there's a string of the same number
    while (i + count < len(l)):
      if current == l[i + count]:
          count = count + 1
      else:
        tups.append((current, count))
        break

    # special check for the end of the list
    if i + count == len(l):
      tups.append((current, count))

    i = i + count

  return tups

# tests
def main():
  l1 = [1, 1, 1, 2, 3, 3, 4]
  l2 = []
  l3 = [1, 1, 1, 1]
  l4 = [1, 1, 1, 2, 3, 3, 4, 4]

  print run_length(l1)
  print run_length(l2)
  print run_length(l3)
  print run_length(l4)

if __name__=='__main__':
  main()
