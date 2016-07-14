#!/usr/bin/python

#
# An example of importing a function from another module
# Daven Farnham
# 2015
#

# import functions from another module
import fun

def main():
    fun.hello_world() # access that module's functions with the '.' operator

# used by the python interpreter to figure out which program in the 'main' one
if __name__ == '__main__':
    main() # execute this function
