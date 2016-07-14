#!/usr/bin/python

import os
import commands

def write_file():
  f = open('test.txt', 'w')

  f.write('This is a sample string\n')

  # close file
  f.close()

  # make a new directory
  os.mkdir('temp')

  # command to run
  cmd = 'mv test.txt temp'

  # run the command
  status, output = commands.getstatusoutput(cmd)

  if status:
    print 'error'

  if not os.path.exists('here.txt'):
    cmd = 'cp temp/test.txt ./here.txt'

    status, output = commands.getstatusoutput(cmd)

    if status:
      print 'error'
  else:
    os.remove('here.txt')

def main():
  write_file()

if __name__=='__main__':
  main()
