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
# try different results
 
# Example:
# input text: Cats, dogs and birds are common pets. So are fish.
# output tokens: cat, dog, bird, common, pet, fish
 
import nltk
 
from nltk.corpus import stopwords
 
str_cat = """The cat is in the box. The cat likes the box. The box is over the cat"""
cat_tokens = [w for w in word_tokenize(str_cat.lower()) if w.isalpha()]
 
no_stops = [t for t in cat_tokens if t not in stopwords.words('english')]
 
Counter(no_stops).most_common(2)

str_path = '/Volumes/ORANGE/Documents/Projects/BigData/Skills/Python/NLTK-2.0/data_camp/chapter_2/article.txt'
f = open(str_path, 'r')
article = f.read()


from collections import Counter

tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]

lower_tokens_no_stops = [t for t in lower_tokens if t not in stopwords.words('english')]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens_no_stops)

# Print the 10 most common tokens
print(bow_simple.most_common(10))

# =====================================================================
# =====================================================================
# =====================================================================
# Simple Text Preprocess =============================================
# =====================================================================

# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer


# Retain alphabetic words: alpha_only  --- so this gets rid of all sorts of things
# -- like punctuation and and dates...
alpha_only = [t for t in lower_tokens_no_stops if t.isalpha()]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in alpha_only]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))























