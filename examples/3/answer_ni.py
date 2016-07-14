#!/usr/bin/python
import re

def count():
  f = open('holy_grail.txt', 'r')
  
  script = f.read()
  
  print len(re.findall(r'[Kk]nights Who Say ["]*Ni["]*', script))

  f.close()

def main():
  count() # 6 + 4 = 10
  
if __name__=='__main__':
  main()