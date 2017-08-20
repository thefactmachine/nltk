#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 11:18:43 2017

@author: markhatcher
"""

# For loop with two variables
names = ( "John", "Sal", "Bill" )
ids = ( 123, 321, 231 )
lst_tup = zip(names, ids)
 
# this gives a list of tuples
#  [('John', 123), ('Sal', 321), ('Bill', 231)]
 
for x, y in lst_tup:
    print("this is x: " + x + " and this is y: " + str(y))
# =============================================================
# =============================================================
# =============================================================
# =============================================================
# Named Entity Recognition ===================================
# =============================================================

# NLP is to identify important named entities in the text....
# People, places and organisations.
# They can be dates, states and works of art depending on the 
# libraries that you use....

# Can b use used alongside topic identification ...or...on its own
# to identify Who? What? When? Where?

# There is a stanford NER libaries....

# NER can be used for fact extraction...

# NER can determine which entities are related using computational language
# models....

# Token proximity...enables relationships...

# Stanford libary requires Java files and system environment variables...

# =============================================================
# Exercise 3.1 ================================================
 
import codecs
import nltk

str_uber_path = (r'/Volumes/ORANGE/Documents/Projects/BigData/'
                 r'Skills/Python/NLTK-2.0/data_camp/chapter_2/'
                 r'uber_article.txt')
str_uber_path


# see below for thing on unicode.
f = codecs.open(str_uber_path, 'r',  encoding = 'utf-8')
article = f.read()

# get the blob of text...and then create sentences.....
sentences = nltk.sent_tokenize(article)
 
len(sentences)

# Tokenize each sentence into words: token_sentences
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]

# this is actually broken up into lists of lists....
len(token_sentences)
token_sentences[0]


# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 

print nltk.ne_chunk(pos_sentences[2], binary = True)

len(pos_sentences)

# Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)

# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)
            
test = []
for sent in chunked_sentences:
    for chunk in sent:
        test.append(chunk)
        
# =============================================================
sent  = nltk.corpus.treebank.tagged_sents()[22]
print nltk.ne_chunk(sent, binary = True)
        
            
utf_test = pos_sentences[2][0][1]
utf_test

# convert a byte string to a Unicode string
utf_test.decode('utf-8')

# =============================================================
# =============================================================
# =============================================================
# lets see if we can fix sentence two

sent_two = utf_test = pos_sentences[2]
sent_two_fix = []
for tup in sent_two:
    temp_pos = tup[1]
    temp_pos = temp_pos.decode('utf-8')
    temp_word = tup[0]
    temp_tup = (temp_word, temp_pos)
    sent_two_fix.append(temp_tup)

print nltk.ne_chunk(sent_two_fix, binary = True)



# encode converts a unicode string to byte string
jj = []
for a in enumerate(sent_two):
    temp = a[1][1]
    temp = temp.decode('utf-8')
    jj.append(temp)
    indx = a[0]
    print sent_two[indx]



            












