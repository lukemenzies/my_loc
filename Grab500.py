#!/usr/bin/python
# Get500.py
# This script grabs the first 500 lines of a text file
# so I can test scripts on the text file without inputting
# the whole 425MB text.

import sys, os

# homedir = os.getcwd()
homedir = raw_input("What is the working directory? ")
print("From what file will the lines be taken (including extension)?")
srcfile = os.path.join(homedir, raw_input("    : %s/" %homedir))
print("What will the new file be named (including extension)?")
dstfile = os.path.join(homedir, raw_input("    : %s/" %homedir))
linenum = 0
with open(dstfile, 'w') as ofile:
    with open(srcfile, 'r') as ifile:
        while linenum < 500:
            line = ifile.readline()
            ofile.write(line)
            linenum += 1
            print("line: %d" %linenum)
