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
 
