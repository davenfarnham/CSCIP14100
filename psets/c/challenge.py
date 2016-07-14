#!/usr/bin/python

### HELPER FUNCTIONS ###

# Your old friend fold
def fold(f, l, i):
  if len(l) == 0:
    return i
  if len(l) == 1:
    return f(l[0], i)
  else:
    return f(l[0], fold(f, l[1:], i))

# Takes a string and returns it in list for. For example:
#
#   string_to_list('hello') == ['h', 'e', 'l', 'l', 'o']
#
def string_to_list(s):
  initial = []

  for i in s:
    initial.append(i)

  return initial

### QUESTIONS ###

# CHALLENGE ONE: Takes a list of lists and returns only those lists that have 3
# or more elements in them. For example:
#
#   long_list[[1, 2, 3], [4, 5], [6, 7, 8, 9]] == [[1, 2, 3], [6, 7, 8, 9]]
#
# Hint: You're going to want to use both filter and fold!
def long_list(s):

  return 'TODO'

# CHELLENGE TWO: Takes two parameters, a string and the length of the string, and
# reverses the characters. YOU MUST DO THIS RECURSIVELY. So:
#
#   reverse('dragon', 6) == 'nogard'
#
def reverse(s, n):

  return 'TODO'

# main, with some functions to help test the above functions
def main():
  # test long_list. Should print [[1, 2, 3], [6, 7, 8, 9]]
  print long_list([[1, 2, 3], [4, 5], [6, 7, 8, 9], [], [10]])

  # tests for reverse
  s = 'dragon'
  s1 = 'hello'
  s2 = 'h'
  s3 = ''

  print reverse(string_to_list(s), len(s))    # print 'nogard'
  print reverse(string_to_list(s1), len(s1))  # print 'olleh'
  print reverse(string_to_list(s2), len(s2))  # print 'h'
  print reverse(string_to_list(s3), len(s3))  # print ''

if __name__=='__main__':
  main()
