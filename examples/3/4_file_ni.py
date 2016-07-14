#!/usr/bin/python
import re

def count():
  f = open('holy_grail.txt', 'r')
  out = open('output.txt', 'w')

  count = 0
  
  # reads in one line at a time
  for line in f:
    match = re.findall(r'Knights Who Say ["]*Ni["]*', line)
    if match:
      out.write(line + '\n')
      count = count + len(match)

  print count

  f.close()
  out.close()

def main():
  count() # 6 + 4 = 10
  
if __name__=='__main__':
  main()