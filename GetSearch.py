#!/usr/bin/python3
# this script does several things...

import os, requests

s = input("What query? ")
w = input("what outfile name? ")
homedir = input("What home directory? ")
outfile = homedir+w+'OCR.txt'
outfile2 = homedir+w+'URLs.txt'
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
#                ofile2.write("item number %d" %itnbr)
                ofile2.write("\n")
                itnbr = itnbr + 1
                urlsnum = urlsnum + 1
print("number of urls: %d " %urlsnum)
wait = input("Continue (y/n)?")
filenum = 1
with open(outfile2, 'r') as ofile3:
    for lines in ofile3:
        num = str(filenum)
        line = lines[:-1]
        command = "wget -O "+newdir1+w+"-%s.pdf "%num+line
#        print(command)
        os.system(command)
        filenum = filenum + 1
filenum = filenum - 1
print("number of files downloaded: %d " %filenum)
