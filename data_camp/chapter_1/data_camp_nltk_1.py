#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 18:44:04 2017

@author: markhatcher
"""

# =================BASICS OF NLTK =============================================
# ===========================================================================
# === START =====START ============START=============START==================
# ===========================================================================
import re
 
# pattern always comes first, string is the second argument
# this returns a match object
match_obj = re.match('abc', 'abcdef')
match_obj.group()
match_obj.start()
match_obj.end()
match_obj.re
 
word_regex = '\w+'
wrd_regex = re.match(word_regex, 'hi there! mark')
 
# word, digit, space  -- word is full word rather than one character
# \w+ \d \s
# negation is capitals....capital s ((i.e. S)) anything that is not a space
# regex verbs:  split, findall, search, match
# these verbs may return an iterator, string or a match object
re.split('\s+', 'split on spaces.')
 
# returns this:  ['split', 'on', 'spaces.']
 
my_string = "Let's write RegEx!"
pattern = r'\w+'
re.findall(pattern, my_string)
# returns this:  ['Let', 's', 'write', 'RegEx']
 
pattern = r'\s+'
re.findall(pattern, my_string)
# returns this: re.findall(pattern, my_string)
 
pattern = r'\w'
re.findall(pattern, my_string)
# ['L', 'e', 't', 's', 'w', 'r', 'i', 't', 'e', 'R', 'e', 'g', 'E', 'x']
 
# ==== Exercise 1 =========================================================
 
str_my_string = """Let's write RegEx? Won't that be fun! I sure think so. Can you find 4 sentences? Or perhaps, all 19 words"""
print(str_my_string)
 
 
import re

sentence_endings_a = r'\?|!|\.'
sentence_endings_a
 
l = re.split(sentence_endings_a, str_my_string)
l
print("length is " + str(len(l)))
 
 
 
sentence_endings_b = r'[\?!\.]'
sentence_endings_b
a = re.split(sentence_endings_b, str_my_string)
a
len(a)
# A word character is a character from a-z, A-Z, 0-9, including the _ (underscore) character.
 
 
rex_ex= r'\d+'
rex_ex
re.findall(rex_ex, str_my_string)
 
# ==== Exercise 2 =======================tokenizing===============================
 
# reasons for tokenizing: map part of speech, match common words, remove unwanted tokens
# nltk tokenizers:
# sent_tokenize ---- sentences
# regexp_tokenize --- reg_ex
# tweetTokenize ---- tweets
 
# re.match  -- at the begining of a string -- every pattern has ^
# re.search -- throughout the entire string
# re.match('pattern') equals re.search('^pattern')
str_path = '/Volumes/ORANGE/Documents/Projects/BigData/Skills/Python/NLTK-2.0/data_camp/chapter_1/example_text.txt'


f = open(str_path, 'r')
message = f.read()
print(message)
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
 
# Split scene_one into sentences: sentences
sentences = sent_tokenize(message)
for s in sentences:
    print(s)
 
sentences[0:5]
    
# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])
 
# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(message))
print(unique_tokens)
 
# ==== Exercise 3 ============more======tokenizing===============================
 
match = re.search("coconuts", message)
print(match.start(), match.end())
 
pattern1 = r"\[.*\]"
print(pattern1)
 
# Use re.search to find the first text in square brackets
re.search(pattern1, message)

search = re.search(pattern1, message)

# how to use re.search
if re.search("mark", "this is mark space"):
    print("found it")
else:
    print("did not find it")
 
    
    
    
    
test = re.search("mark", "this is mark space")
test.start()
test.end()
 
 
# ==== Exercise 4 ============more======tokenizing===============================
 
import re
rgx_wrd_digit = r'(\d+|\w+)'
rgx_wrd_digit
re.findall(rgx_wrd_digit, 'he has 11 cats')
 
# [A-Za-z\-\.]+  ==== matches 'My-Website.com'
# groups are different
# (a-z)  matches "a-z"
 
 
tweet0 = r'This is the best #nlp exercise ive found online! #python'
print(tweet0)
 
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
 
# hash tags
pattern1 = r"#\w+"
regexp_tokenize(tweet0, pattern1)

 
tweet2 = r'Thanks @datacamp :) #nlp #python'
# mentions and hashtags
pattern2 = r"([#|@]\w+)"
regexp_tokenize(tweet2, pattern2)
 
tknzr = TweetTokenizer()
lst_tweets = ['This is the best #nlp exercise ive found online! #python',
              '#NLP is super fun! <3 #learning',
              'Thanks @datacamp :) #nlp #python']
   
all_tokens = [tknzr.tokenize(t) for t in lst_tweets]
all_tokens
 
