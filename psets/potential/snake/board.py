#!/usr/bin/env python
import sys
from sys import stdout
import time
from msvcrt import getch

def print_board():
  # print out board
  stdout.write ('------------------------------------------\n')
  for i in range (0, 12):
    stdout.write ('|                                        |\n')
  stdout.write ('------------------------------------------\n')

  key = ord(getch())

  # escape sequence to possibly erase users' input
  stdout.write ('\x1b[2K')

  # wait for a quarter of a second
  time.sleep(.25)
  
  # terminal code for moving up in terminal window
  jump = ['\033[1A']
  
  # jump up 12 lines in the terminal
  for j in range(0, 14):
    stdout.write(jump[0] + '\r')

  # flush buffer  
  stdout.flush()

