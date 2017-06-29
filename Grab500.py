#!/usr/bin/python3
# this script grabs the first 500 lines of a text file
# so I can test scripts on the text file without inputting
# the whole 425MB text

import sys

Homedir = raw_input("What home directory? ")
SrcFile = Homedir+raw_input("What source file? ")
DstFile = Homedir+raw_input("What is the new file? ")
linenum = 0
with open(DstFile, 'w') as ofile:
    with open(SrcFile, 'r') as ifile:
        for line in ifile:
            if linenum < 500:
                ofile.write(line)
            linenum = linenum + 1
            print(linenum)
            if linenum >= 500:
                sys.exit
