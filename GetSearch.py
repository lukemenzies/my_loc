#!/usr/bin/python3
# GetSearch.py uses Python 3
# This script does several things using GNU Wget and ChronAm:
# (a) runs a search using the Chronicling America API
# (b) downloads PDF images for the search results
# (c) extracts OCR text from the results and places it in
#     both a single .TXT file and individual .TXT files.
# *The script creates a file of URLs which it uses to download
# the results with the command "wget -O <destination> <URL>
# Thus, wget must already be installed and working from the command line.
# Created by Luke Menzies for the Library of Congress 6/20/17

import os, requests

print("What is your query? (Enter the string EXACTLY as it will appear in the URL.)")
s = input("    : ")
print("What is the base name for the results? (Do not include an extension.)")
w = input("    : ")
print("What is the working directory? ")
print("(Include fore and aft slashes.)")
homedir = input("    : ")
# homedir = os.getcwd()
if not os.path.exists(homedir):
    os.mkdir(homedir)
outfile = os.path.join(homedir, "%s_OCR.txt" %w)
outfile2 = os.path.join(homedir, "%s_URLs.txt" %w)
search1 = "http://chroniclingamerica.loc.gov/search/pages/results/?proxtext="+s+"&language=eng&format=json"
totalItems = requests.get('%s' %search1).json()['totalItems']
print("Total Items: %d " %totalItems)
pag = round((totalItems / 20) + 0.499)
print("Total Pages: %d " %pag)
pages = pag + 1
urlsnum = 0
itnbr = 0
newdir1 = homedir+w+"-PDFs/"
newdir2 = homedir+w+"-TXTs/"
if not os.path.exists(newdir1):
    os.mkdir(newdir1)
if not os.path.exists(newdir2):
    os.mkdir(newdir2)
with open(outfile, 'w') as ofile:
    with open(outfile2, 'w') as ofile2:
        for x in range(1, pages):
            num = str(x)
            search = "http://chroniclingamerica.loc.gov/search/pages/results/?proxtext="+s+"&language=eng&page="+num+"&format=json"
#            print("search, page %s: " %num, search)
            print("Page %s of %d " %(num, pag))
            r = requests.get('%s' %search).json()
            for item in r['items']:
                z = str(itnbr + 1)
                outfile4 = newdir2+w+"OCR-%s.txt" %z
                with open(outfile4, 'w') as ofile4:
                    ofile4.write(item['ocr_eng'])
                ofile.write(item['ocr_eng'])
                newurl = str(item['url']).replace('.json', '.pdf')
                ofile2.write(newurl)
                ofile2.write("\n")
                itnbr += 1
                urlsnum += 1
print("Total number of URLs: %d " %urlsnum)
# wait = input("Enter to continue.")
filenum = 1
with open(outfile2, 'r') as ofile3:
    for lines in ofile3:
        num = str(filenum)
        line = lines[:-1]
        command = "wget -O "+newdir1+w+"-%s.pdf "%num+line
#        print(command)
        os.system(command)
        filenum += 1
filenum = filenum - 1
print("Total number of files downloaded: %d " %filenum)
