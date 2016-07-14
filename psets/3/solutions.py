#!/usr/bin/python
import re
import os

### DIFFICULTY OUT OF 3 STARS (***) ###

# Irregular Expressions
# Note: don't use actual words in your answers, only patterns. For example, say
# I want to match the name 'Rob', then your regex could be r'\w\w\w' or r'\w{3}', but
# not r'Rob'

# 1.10 Emails ( * )
# Using a SINGLE regular expression, extract from the list of emails below those that look real.
# To be real, the email has to have at least one character before the '@' (so it can't be blank and
# it can't be only digits). After your regex returns, you should have a list of 6 email addresses. Return
# that list.
def emails():
    
    # create list of emails
    emails = 'daven.farnham@gmail.com daven@cs50.net malan@harvard.edu mike@aol.com @netscape.com'
    emails = emails + ' 123456@sina.com rob@harvard.cs.edu zabie94@gmail.com' 
    
    match = re.findall(r'[a-z]+[.]*\w*@\w+[.]\w+[.]*\w*', emails)
    
    return match
    
    
# 1.11 Bling Bling ( *** )
# Steve, who works at the bank, accidently saved everyone's credit card numbers in plaintext, meaning
# if I were to open creditcards.txt I could see everyone's CC information. Your task is to
# programmatically cover the credit card numbers up.
#
#                       1) open up the file creditcards.txt
#                       2) using a regex find the CC numbers, name, phone #s, etc
#                       3) cover up part of the CC number, for example if the # is: 378282246310005
#                          you might want to substitute in 3782*********** leaving only the first 4 numbers
#                       4) write out all the data, with the now covered up CC #, to a new file named encrypted.txt
#                       5) delete the original file you were working with (creditcards.txt)
#
def numbers():
  
  # open file
  f = open('creditcards.txt', 'r')
  
  # list to put information in
  l = []
  
  # iterate through lines in file, adding info to l
  for line in f:
    match = re.findall(r'([A-Z][a-z]+)|(\d+)|(\d{16}|\d{15}|\d{14})', line)
    if match:
      length = len(match[2][1])
      l.append((match[0][0], match[1][1], match[2][1], length))
      
  f.close()
  
  # remove the file you just iterated through
  os.remove('creditcards.txt')
  
  # open a new file
  out = open('encrypted.txt', 'w')
  
  # write out
  for num in l:
    name, phone, word, size = num
    out.write(name + ', ' + phone + ', ' + word[0] + word[1] + word[2] + word[3] + '*' * (size - 4) + '\n')

  out.close()
 
# Recursion ... recursion ... recursion ...
# 1.2 'A car, a man, a maraca' ( ** )
# Given a word 's' with NO SPACES, using recursion tell whether the word is a palindrome,
# meaning it's spelled the same way forward as backward
def palindrome(s):
  if len(s) == 0 or len(s) == 1:
    print 'palindrome'
  elif s[0] != s[len(s) - 1]:
    print 'not palindrome'
  else:
    palindrome(s[1:-1])

# On a higher place of thinking
# On the next few questions, make sure to use a higher order function, so either: map, reduce, or filter
# 1.3 ( ** ) Retain only the odd numbers in a list
def filter_odd(l):
  print filter(lambda x: x % 2 != 0, l)
    
# A helpful higher order function, kind of like reduce but a little different    
def fold(f, l, i):
  if len(l) == 1:
    return f(l[0], i)
  else:
    return f(l[0], fold(f, l[1:], i))
    
# 1.3.1 ( *** ) Returns the number of times a number occurs in a list. So num_occurs(4, [1, 2, 3, 4, 4, 5, 4]) == 3
# In this function you have to use the above fold() function, so read it and make sure you know how it 
# works before attempting num_occurs()!
def num_occurs(n, l):
  print fold(lambda x, y: 1 + y if x == n else 0 + y, l, 0)


# 1.4 ( *** ) It's learning! (aka the beginning of skynet)
# Last week we made a dictionary of words. As just a refresher:
#
#                     1) We opened the dictionary file
#                     2) Read it into a string
#                     3) split the string up using .split() into a list
#                     4) Then placed all the words into a dictionary
#
# Our dictionary last week was good, but a bit basic. For example we
# all know in real life new words are added to what's generally accepted
# as 'correct' all the time. In the function learning_dict() you're going
# to import dict.txt and put the words into a dictionary. You'll then run
# your dictionary on holy_grail.txt from yesterday.
#
# You're not done yet, though. If the SAME word appears mispelled more than 
# THREE times, instead of counting it as a mispelled word, add it to the
# dictionary and treat it as a correct word. In this way, the dictionary
# 'learns' based on the frequency of words it comes across.
def learning_dict():
  correct_dict = {}
  
  # open dictionary
  f = open('words.txt', 'r')
  words = f.read().split()
  
  # put into dictionary
  for word in words:
    correct_dict[word.lower()] = None

  o = open('holy_grail.txt', 'r')
  s = o.read()

  # split holy_grail.txt based on whitespace
  script = s.split()
  
  # dictionaries for debugging
  incorrect_dict = {}
  added = {}
  
  # number of mispelled words
  count = 0
  
  for l in script:
    # add regular expression to deal with periods
    match = re.search(r'[\"]*(\w+)[\".!,?,/]*',l)
    if match:  
      l = match.group(1)
    # turn all words in string to lower case to match dictionary
    if l.lower() not in correct_dict:
      if l.lower() not in incorrect_dict:
        incorrect_dict[l.lower()] = 1
        count = count + 1
      elif incorrect_dict.get(l.lower()) == 1:
        incorrect_dict[l.lower()] = 2
        count = count + 1
      else:
        incorrect_dict.pop(l.lower())
        count = count - 2
        correct_dict[l.lower()] = None
        added[l.lower()] = None
  
  print added 
  print '\n\n'
  print incorrect_dict
  return count


def main():
    emails()
    numbers()
    palindrome('mannam')
    filter_odd([1, 2, 3, 4])
    num_occurs(4, [1, 2, 3, 4, 4, 5, 4])
    print learning_dict()

if __name__=='__main__':
  main()