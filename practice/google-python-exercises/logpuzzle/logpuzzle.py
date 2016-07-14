#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import shutil

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # first find base server from filename
  base = re.search(r'_([\w.]+)', filename).group(1)

  # open file log
  f = open(filename, 'r')
  
  # read file into single string
  text = f.read()
  
  # get all urls (O(n) where n == # of strings in the file)
  urls = re.findall(r'GET ([\w./~-]+) HTTP/1.0', text) 
  
  # filter based on whether the word 'puzzle' is in the URL (O(m) where m == # of string urls)
  puzzle_urls = filter(lambda x: re.search(r'puzzle', x), urls)

  # see if there are two words in the url
  two_words = (re.findall(r'puzzle/\w+([-]\w+)([-]\w+)', puzzle_urls[0]))
  
  # bad, since I'm essentially reusing the code above, but return the second match in the tuple
  def sec_word(str):
    tuple = (re.findall(r'puzzle/\w+([-]\w+)([-]\w+)', str))
    one, two = tuple[0]
    return two
  
  # if there are, sort by the second word
  if two_words != []:
    if len(two_words[0]) > 1: 
      sorted_puzzle_urls = sorted(list(set(puzzle_urls)), key = sec_word)
  else:
    # turn to set to eliminate duplicates, then back to a list to sort. (set() == O(1); list is probably the same; sorted is O(klogk))
    sorted_puzzle_urls = sorted(list(set(puzzle_urls)))

  # add base to all urls (O(k) where k == # of urls in sorted list [no duplicates] [have the word puzzle in them])
  with_base = map(lambda x: 'http://' + base + x, sorted_puzzle_urls)     
  
  # close file
  f.close()
    
  # total complexity = O(klogk + n + m + k) = O(klogk)   
  return with_base
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # if dir doesn't exist, create it
  if not os.path.exists(dest_dir):  
    os.mkdir(dest_dir)
    
  # counter for changing the value of the destination img
  count = 1  
    
  # let user know it's working  
  print 'retrieving...'

  # open index file
  f = open('index.html', 'w')

  # move index file to new dir
  shutil.move(os.path.abspath('index.html'), dest_dir)

  # write header info to index.html
  f.write('<html>\n<body>\n')

  # go through list of urls dl'ing the data and creating files 
  for url in img_urls:
    urllib.urlretrieve(url, 'img' + str(count))
    # move to newly created folder
    path = os.path.abspath('img' + str(count))
    shutil.move(path, dest_dir)
    path = os.path.abspath(dest_dir + '/img' + str(count))
    # write to index file
    f.write('<img src =' + '"' + path + '"' + '>')
    count = count + 1
  
  # write last bit of html  
  f.write('\n</body>\n</html>')
  
  # close the file
  f.close()
      
  return
    
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
