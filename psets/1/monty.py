#!/usr/bin/python

#
# Question 2.1
#
# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
#
# So, for example, if I pass the lists l = [1, 3, 5] and r = [2, 4, 6], I should
# get back [1, 2, 3, 4, 5, 6]
#
def list_merge(l, r):

#
# Question 2.2
#
# Run length encoding for compression. This is BIG in compressing files. The basic
# idea is, say I pass in a list l = [1, 1, 2, 3, 4, 4, 5], run_length(l) should return
# a list of tuples where the first element is the content of the list and the second
# element is how many times that element appears in a row. So, run_length(l) should
# return: [(1, 2), (2, 1), (3, 1), (4, 2), (5, 1)]
#
def run_length(l):
