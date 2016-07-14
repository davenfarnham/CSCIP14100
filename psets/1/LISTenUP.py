#!/usr/bin/python

#
# Question 1.1 (Say My Name)
# 
# Below is a list of strings (single characters). They aren't in order though =/ 
#
# First, order the list below alphabetically. Then, after you've ordered it, recreate 
# the sentence 'python is awesome' by indexing into the array.
#
# For example, if I had a list l = ['1', '2'] and wanted to create a new number, I could do:
#
#                   num = int(l[1] + l[0])      # should give me the number 21
#
# After you're done, return the string!
#

def say_my_name():

  alpha = ['z', 'a', 'b', 'y', 'c', 'x', 'd', 'w', 'e', 'v', 'f', 'g', 'u', 'h', 'i', 'j', 't' 'k', 'l', 's', 'm', 'n', 
            'r', 'o', 'p', 'q', ' ']  
            
    # TODO
            
#
# Question 1.2 (Order's up!)
#
# Given a list of strings, sort them based on their length AND middle character. If a
# string has an even numbers of characters, sort by the (n/2 + 1) index.
# You can assume you won't be passed the empty string.
#
def string_sort(words):
    # TODO
