#!/usr/bin/python

import re

def parse():
    f = open('class.csv', 'r')

    out = open('numbers.txt', 'w')

    for line in f:
      match = re.findall(r'[A-Z]\w+|\d\d\d-\d\d\d-\d\d\d\d', line)
      if match:
        out.write(match[0] + ': ' + match[1] + '\n')

    f.close()
    out.close()

def main():
    parse()

if __name__=='__main__':
    main()
