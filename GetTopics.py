#!/usr/bin/python
# this script takes a directory of .txt files and
# (a) remove stopwords, punctuation, etc.
# (b) come up with a list of 10 topics
# based on the tutorial by Radim Rehurek
# at http://rare-technologies.com/tutorial-on-mallet-in-python/
# composed by Luke Menzies for LoC 6/19/17

import os, sys
from gensim import corpora, models, utils
from gensim.models.wrappers.ldamallet import LdaMallet

def iter_documents(input_dir):
    for fname in os.listdir(input_dir):
        # read each document as one big string
#        print("opening: %s" %fname)
        with open(os.path.join(input_dir, fname), 'r') as docu:
            document = docu.read()
#        document = open(os.path.join(input_dir, fname)).read()
        # parse document into a list of utf8 tokens
            yield utils.simple_preprocess(document)

class NewCorpus(object):
    def __init__(self, input_dir):
        self.input_dir = input_dir
        self.dictionary = corpora.Dictionary(iter_documents(input_dir))
        self.dictionary.filter_extremes()  # remove stopwords etc

    def __iter__(self):
        for tokens in iter_documents(self.input_dir):
            yield self.dictionary.doc2bow(tokens)

# set up the streamed corpus
Homedir = '/Users/lmenzies/Documents/1Docs2017/SU17/LoC/LoC4Robots/'
# Homedir = input("What is the working directory? ")
print("In what directory are the txt files for the new corpus?")
corpusdir = Homedir+input("    %s" % Homedir)
if not os.path.exists(corpusdir):
    print("Directory does not exist.")
    print("Quitting... Please try again.")
    sys.exit
print("In what directory will the results be placed? ")
print("(If it does not exist, it will be created.)")
outpath = Homedir+input("    %s" % Homedir)
topics = int(input("How many topics? "))
if not os.path.exists(outpath):
    os.mkdir(outpath)
# deletes .DS_Store file (for Macs)
ds_store1 = corpusdir+".DS_Store"
if os.path.exists(ds_store1):
    os.remove(ds_store1)
ds_store2 = outpath+".DS_Store"
if os.path.exists(ds_store2):
    os.remove(ds_store2)
corpus = NewCorpus(corpusdir)
# train 20 LDA topics using MALLET
# mallet_path = input("What is the path to mallet (including \'bin/mallet\')? ")
mallet_path = '/mallet-2.0.7/bin/mallet'
model = models.wrappers.ldamallet.LdaMallet(mallet_path, corpus, num_topics=topics, id2word=corpus.dictionary, prefix=outpath)
modoutfile = os.path.join(outpath, "model_01")
with open(modoutfile, 'w') as printfile:
     for item in model[corpus]:
        printfile.write(str(item))
