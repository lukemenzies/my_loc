#!/usr/bin/python
# GetTopics.py uses Python 3
# This script takes a directory of .txt files and
# (a) removes stopwords, punctuation, etc.
# (b) produces a list of 'n' topics
# This is based on the tutorial by Radim Rehurek at:
# http://rare-technologies.com/tutorial-on-mallet-in-python/
# Adapted for the Library of Congress by Luke Menzies, 6/19/17.

import os, sys
from gensim import corpora, models, utils
from gensim.models.wrappers.ldamallet import LdaMallet

def iter_documents(input_dir):
# reads each document as one big string and parses it as UTF8 tokens
    for fname in os.listdir(input_dir):
        with open(os.path.join(input_dir, fname), 'r') as docu:
            document = docu.read()
            yield utils.simple_preprocess(document)

class NewCorpus(object):
    def __init__(self, input_dir):
        self.input_dir = input_dir
        self.dictionary = corpora.Dictionary(iter_documents(input_dir))
        self.dictionary.filter_extremes()  # remove stopwords etc

    def __iter__(self):
        for tokens in iter_documents(self.input_dir):
            yield self.dictionary.doc2bow(tokens)

# homedir = os.getcwd()
homedir = input("What is the working directory? ")
print("In what directory are the TXT files for the new corpus? (Include a final slash.)")
corpusdir = os.path.join(homedir, input("    : %s/" %homedir))
if not os.path.exists(corpusdir):
    print("Directory does not exist.")
    print("Please try again. Quitting... ")
    sys.exit
print("In what directory will the results be placed? (Include a final slash.) ")
print("If it does not exist, it will be created.")
outpath = os.path.join(homedir, input("    : %s/" %homedir))
topics = int(input("How many topics? "))
if not os.path.exists(outpath):
    os.mkdir(outpath)
# the next few lines delete the .DS_Store file (for Macs)
ds_store1 = os.path.join(corpusdir, ".DS_Store")
if os.path.exists(ds_store1):
    os.remove(ds_store1)
ds_store2 = os.path.join(outpath, ".DS_Store")
if os.path.exists(ds_store2):
    os.remove(ds_store2)
corpus = NewCorpus(corpusdir)
# trains 'n' LDA topics using MALLET
mallet_path = input("What is the path to mallet (including \'bin/mallet\')? ")
# mallet_path = '/mallet-2.0.7/bin/mallet'
model = models.wrappers.ldamallet.LdaMallet(mallet_path, corpus, num_topics=topics, id2word=corpus.dictionary, prefix=outpath)
modoutfile = os.path.join(outpath, "model_01")
with open(modoutfile, 'w') as printfile:
     for item in model[corpus]:
        printfile.write(str(item))
