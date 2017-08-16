#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:10:25 2017

@author: markhatcher
"""

# BAG OF WORDS
# Basic method for finding topics in text
# 1) First create tokens using tokenisation
# 2) Count up all tokens..
# 3) Theory is that the most popular word characterizes the text.
# 4  Great way of finding the significance of words in text.
 
from nltk.tokenize import word_tokenize
from collections import Counter
 
str_a = """The cat is in the box. The cat likes the box. The box is over the cat"""
 
lst_tokens = word_tokenize(str_a)
counter_tokens = Counter(lst_tokens)
counter_tokens.most_common(5)
 
# =====================================================================
 
# how to convert a list to lower case.....or uppp
[t.upper() for t in lst_tokens]
 
# PREPROCESSING ------
# examples: tokenisation, lower_casing words, lemmatization / stemming
# removing stop words, punctuation, unwanted tokens
# plural nouns singular
 
# Example:
# input text: Cats, dogs and birds are common pets. So are fish.
# output tokens: cat, dog, bird, common, pet, fish
 
import nltk
 
from nltk.corpus import stopwords
 
str_cat = """The cat is in the box. The cat likes the box. The box is over the cat"""
cat_tokens = [w for w in word_tokenize(str_cat.lower()) if w.isalpha()]
 
no_stops = [t for t in cat_tokens if t not in stopwords.words('english')]
 
Counter(no_stops).most_common(2)

