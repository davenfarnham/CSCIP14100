#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  
  # open the file
  f = open(filename, 'r')
  
  # create an empty dictionary
  dict = {}

  # give year more scope
  year = 0
  
  # iterate over the file's lines (runs in O(n) where n is the number of lines in the file)
  for line in f:
    # match h3 line
    h3 = re.search(r'h3[^/]+' ,line) # can you match anything up to a string, not just a char (^\w)?
    if h3:
        year = (re.search(r'\d\d\d\d', h3.group())).group() # find year
    else:
        names = re.findall('<td>\w+', line) # find all occurences of <td>
        if names:
          rank = str((names[0]))[4:] # use slices to jump over tags
          boy = str((names[1]))[4:]
          girl = str((names[2]))[4:]
          # if either of these keys are already in the dictionary, don't put them in again
          if boy in dict.keys() or girl in dict.keys():
            continue
          else:   
            dict[boy] = rank
            dict[girl] = rank

        
  # close file
  f.close()

  # get the items out of the dict; returns list of tuples (O(m) in the worst case where m is the number of things in the dictionary)
  items = dict.items()

  # create empty list
  expanded = []

  # for each list item (rank, (boy's name, girl's name)) (O(m))
  for i in items:
    name, rank = i # match on tuple
    expanded.append(name + ' ' + rank) # put name and rank into list

  # sort list (O(nlogn))
  sorted_list = sorted(expanded)
  
  # concatenate year onto list
  sorted_with_year = [year] + sorted_list

  # return list (total complexity = 2*O(m) + O(n) + O(nlogn) -> O(nlogn) which should be the bound since I'm sorting)
  return sorted_with_year
    
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  output = extract_names(args[0])
  if summary:
    if len(args) != 2:
      print 'Please give me an output file.'
      return
    else:
      f = open(args[1], 'w')
      for i in range (len(output)):
        f.write(str(output[i]) + '\n')
      f.close
  else:
    for i in range (len(output)):
      print output[i]
      
if __name__ == '__main__':
  main()
