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
def long_list(s):
  return filter(lambda z: fold(lambda x, y: y + 1, z, 0) > 2, s) 

# CHALLENGE TWO: Takes two parameters, a string and the length of the string, and
# reverses the characters. So:
#
#   reverse('dragon', 6) == 'nogard'
#
def reverse(s, n):
  if n == 0:
    return ''
  elif n == 1:
    return str(s[0])
  else:
    return (reverse(s[1:], n - 1)) + str(s[0])

# main, with some functions to help test the above functions    
def main():
  # test long_list
  print long_list([[1, 2, 3], [4, 5], [6, 7, 8, 9], [], [10]])
  
  # test string_to_list
  print string_to_list('bigbang')
  
  # tests for reverse
  s = 'dragon'
  s1 = 'hello'
  s2 = 'h'
  s3 = ''
  
  print reverse(string_to_list(s), len(s))
  print reverse(string_to_list(s1), len(s1))
  print reverse(string_to_list(s2), len(s2))
  print reverse(string_to_list(s3), len(s3))
  
if __name__=='__main__':
  main()