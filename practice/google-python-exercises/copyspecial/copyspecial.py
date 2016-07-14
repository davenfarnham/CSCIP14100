#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
def get_special_paths(dir):
  # get filenames in the directory and return a list. dir itself is a list 
  filenames = os.listdir((dir[0]))

  # filter out all files that aren't special
  filenames = filter(lambda x: re.search('\w*[__]\w*[__][.]\w*' , x), filenames)

  # use an int here so you can index into list
  for i in range (len(filenames)):
    filenames[i] = os.path.abspath(os.path.join(dir[0], filenames[i]))

  # return list of absolute paths  
  return filenames

def copy_to(paths, dir):
  # check if path to directory doesn't exist
  if not os.path.exists(dir):
    os.mkdir(dir) # will make a directory in the current folder

  # copy into new directory
  for path in paths:
    shutil.copy(path, dir)  
  
  # return
  return

def zip_to(paths, zippath):
  # make command with zip and path
  cmd = 'zip -j ' + zippath
  
  # add all files in paths to cmd
  for path in paths:
    cmd = cmd + ' ' + path
  
  # print out cmd to make sure it is correct
  print "Command I'm going to do: %s " % cmd

  # this runs the command 'cmd' and returns its status (non-zero if it failed) and output (string)
  status, output = commands.getstatusoutput(cmd)

  # 0 == False; anything else == True
  if status:
    sys.stderr.write(output) # print to stderr
    sys.exit(1) # exit program
  print(output) # if everything went ok, print results to terminal
  
  return
  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  print tozip

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  if len(args) != 1:
    print 'incorrect arguments'
    sys.exit(1)

  # get the list of special paths
  paths = get_special_paths(args)

  # if todir has not been set, just print 
  if todir == '' and tozip == '':
    for path in paths:
      print path
  
  # copy into directory
  if todir != '':
    copy_to(paths, todir) # copy into directory  
  
  # zip the files
  if tozip != '':
    zip_to(paths, tozip)    
         
      
if __name__ == "__main__":
  main()
