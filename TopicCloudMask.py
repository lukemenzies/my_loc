#!/usr/local/bin/python3
# TopicCloudMask.py
# This script takes the file 'topickeys.txt', output by
# Gensim => MALLET topic modeling, and constructs topic
# clouds for each topic in this file, according to the
# frequency of the words/ keys in each topic.
# The topic clouds are shaped according to a .png silhouette
# mask.
# Created by Luke Menzies for the Library of Congress 6/20/17

import os, collections
from collections import Counter
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

workingdir = '/Users/lmenzies/Documents/1Docs2017/SU17/LoC/LoC4Robots/'
print("What is the current working directory? ")
homedir = os.path.join(workingdir, input("    %s" %workingdir))
# homedir = input("What is the working directory? ")
print("What is the corpus text file? ")
corpus = os.path.join(homedir, input("    %s" %homedir))
print("What is the topic list file? ")
topiclist = os.path.join(homedir, input("    %s" %homedir))
print("What is the image file for the mask? ")
maskpng = np.array(Image.open(path.join(homedir, input("    %s" %homedir))))
topnum = 0
#stopwords = set(STOPWORDS)
#stopwords.add("tho")
with open(topiclist, 'r') as tlist:
    for line in tlist:
        topnum +=1
        words = []
        words = line.split()
        del words[0]
        del words[0]
        count = Counter()
        with open(corpus, 'r') as text:
                for line in text:
                    for word in line.split():
                        if word in words:
                            count[word] += 1
        print("Count = %s" % str(count))
#        cont = input("enter to continue")
        wc = WordCloud(background_color="black", max_words=2000, mask=maskpng).generate_from_frequencies(count)
#            wc.generate(text)
        newmask = "Topic_%s.png" % str(topnum)
        wc.to_file(path.join(homedir, newmask))
#            plt.imshow(wc, interpolation='bilinear')
#            plt.axis("off")
#            plt.figure()
#            plt.imshow(maskpng, cmap=plt.cm.gray, interpolation='bilinear')
#            plt.axis("off")
#            plt.show()
