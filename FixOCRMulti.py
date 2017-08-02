#!/usr/bin/python3
# FixOCR.py uses Python 3
# This script removes the non-alphanumeric characters from a text file.
# It also removes any punctuation not specified in line 66.
# In addition, it joins words that have been split by the endline character.
# This script does NOT add words to the personal word list or exception list.
# The script Wordlists.py does that.
# Finally, it deletes any misspelled words 3-letters or fewer.
# Created by Luke Menzies for the Library of Congress 6/20/17.

import os, sys, enchant
from enchant import DictWithPWL
from os.path import basename

def yes_no(prompt):
    yes = set(['yes','y','ye',''])
    no = set(['no','n'])
    while True:
        q = input("%s" %prompt).lower()
        if q in yes:
            return True
        elif q in no:
            return False
        else:
            print("Please answer 'y' or 'n'")

personalists = True
personalists = yes_no("Do you have personal word and exception lists (y/n)? ")
# the following lines can be edited to prompt the user for a path
# print("What is the path to the working directory? ")
# print("(Include fore and aft slashes.)")
# homedir = input("    : ")
homedir = os.getcwd()
if personalists == True:
    print("Enter the path to the inclusion list: ")
    wordlist = os.path.join(homedir, input("    : %s/" %homedir))
    print("Enter the path to the exclusion list: ")
    exceptlist = os.path.join(homedir, input("    : %s/" %homedir))
    d = enchant.DictWithPWL("en_US", pwl=wordlist, pel=exceptlist)
elif personalists == False:
    d = enchant.Dict("en_US")
print("In what directory are the OCR .txt files located? ")
srcdir = os.path.join(homedir, input("    : %s/" %homedir))
if not os.path.exists(srcdir):
    print("This directory does not exist. Re-run the script and try again.")
    print("Quitting... ")
    sys.exit
print("In what directory would you like the results? ")
print("(If it does not exist, it will be created.)")
dstdir = os.path.join(homedir, input("    : %s/" %homedir))
if not os.path.exists(dstdir):
    os.mkdir(dstdir)
# The following lines delete the Mac file ".DS_Store"
ds_store = os.path.join(srcdir, ".DS_Store")
if os.path.exists(ds_store):
    os.remove(ds_store)
filenum = 0
for files in os.listdir(srcdir):
    srcfile = os.path.join(srcdir, files)
    dstfile = os.path.join(dstdir, files)
    hangword = ""
    with open(dstfile, 'w') as ofile:
        with open(srcfile, 'r') as ifile:
            for line in ifile:
# punctuation that should not be removed is listed in the next line:
                newline = "".join(c for c in line if c.isalpha() or c in " \'-")
                words = newline.split(' ')
                firstword = str(words[0])
                newword = hangword+firstword
                if firstword != "" and hangword != "":
                    if d.check(firstword) == False or d.check(hangword) == False:
                        if d.check(newword) != True:
                            hangword = hangword+" "
                    if d.check(hangword) == True and d.check(firstword) == True:
                        hangword = hangword+" "
                newline = hangword+newline
                words = newline.split(' ')
                hangword = str(words[-1])
                words = words[:-1]
# strips out any words 3-letters or fewer that are misspelled
                words[:] = [wrd for wrd in words if wrd != "" and (len(wrd) > 3 or d.check(wrd) == True)]
                newline = " ".join(w for w in words)
                ofile.write("%s\n" %newline)
    filenum += 1
    print("file no.: %d" %filenum)
