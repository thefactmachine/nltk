#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:49:11 2017

@author: markhatcher
"""


# list of codecs here:  https://docs.python.org/2/library/codecs.html
 
# ==================================================================
# Text processing with Unicode =====================================
# ==================================================================
# ==================================================================
 
# English speaking world uses ASCII. In Europe they use the extended
# Latin Characters Sets.
 
# With Unicode, each character is assigned a number called a code point
# code points are written in the form \uXXX where XXXX is the number
# in 4 digit hex form.
 
# Some encodings use a single byte per code point.  Other encodings
# such as UTK-8 use multiple bytes and represent the the full range
# of unicode characters.
 
# Text in files will be in a particular encoding.  So we need to DECODE
# it into Unicode. Conversely to write out Unicode to file or terminal
# We first need to translate it into a suitable encoding....[ENCODING]
 
# From a Unicode perspective, characters are abstract entities that
# can be realized as one or more glyphs.  Only glyphs can appear on screen
# or on paper.  A font is a mapping from characters to glyphs.
# if your terminal is displaying weird stuff...you should ensure you have
# the correct fonts installed on your system.
 
# We need to know the encoding of a particular file......
 
# THe Python codecs module provides functions to read encoded data into
# Unicode strings and to write out Unicode strings in encoded form.
 
# Note that we can write Unicode-encoded data to a file using
# f = codecs.open(path, 'w', encoding = 'utf-8')
 
# The python specific encoding "unicode_escape" is a dummy encoding
# that converts all non-ASCII characters into their \uXXXX representatons
 
# Code points above the ASCII 0 -127 range but below 256 are represented in
# their two-digit form \xXX ....so using you will see different types
# of u\ codes. 
 #
 
# ==================================================================
# Another article on Unicocde== =====================================
# ==================================================================

#  https://docs.python.org/3/howto/unicode.html
# In the 1980s almost all computers were 8 bit..therefore can hold values
# from 0 to 255.  ASCII codes only went up to 127 which was enough for
# English.  Some machines assigned 128 to 255 for accented characters...
# Eventually a standard for 128 - 255 emerged.

# You could write files in Russian using K018 and French using LATIN1 but
# if you wanted to write a French document that uses some Russian...you
# were stuffed.

# Therefore Unicode emerged.  This uses 16 bit characters.  But it turns
# out that 16 bits is not enough. Actually, unicode uses 0 .. 1,114,111

# The rules for translating a Unicode string into a sequence of characters
# is called encoding.

# If all code-points are represented by 16 bits...then for most characters
# (i.e less than 127 or 255)..a lot of space is occupied by 0 bytes.
# this would be really wasteful for transmitting data.....

# in UTF-8 (Unicode Transformation Format) if the code-point is < 128...
# 1 byte is used...else >= 128...its turned into two or three or four bytes.

 # Encodings dont have to handle every possible Unicode character.
 # The rues for converting a Unicode string into the ASCII encoding is
 # to raise a UnicodeEncodeError if there is a value which is greater than 127
 
 # in Python source code, specific Unicode code points can be written using
 # the \u escape sequence. the \U escape sequence is similar but expects
 # 8 digits not four.
 
 # Another article
 # https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
 
# =====================================================================
# ===================================================================== 

# =====================================================================
# Encode - Decode example.............................................

aa = "this is string example....wow!!!"
example_string_bb = aa.encode('base64', 'strict')
print(example_string_bb)


print(example_string_bb.decode('base64'))

# The errors argument specifies the response when the input string
# cannot be converted due to the encoding rules.....


# chr() is the inverse of ord() and unichr()

# this is an error in Python 2.x
chr(57344)
# use the following:  this prints out u'\ue000'
# which is e = 14 ==> 16^3 * 14
unichr(57344)
# the following prints out 57344
ord(u'\ue000')


# Python hex literals......


 
# '\u0061' = (6 x 16) +  1 = 91
a_character = u'\u0061'
print ord(a_character)
 
a_character_again = u'a'
print ord(a_character_again)
 
check_mark =  u'\u2713'
print(check_mark)

print ("おはよう") 

# ==============================================================================
# ==============================================================================
# ==============================================================================
# The module unicodedata lets us inspect the properites of Unicode characters
# ==================
import unicodedata

u = unichr(233) + unichr(0x0bf2) + unichr(3972) + unichr(6000) + unichr(13231)

list(enumerate(u))

for i, c in enumerate(u):
    print i, '%04x' % ord(c), unicodedata.category(c), unicodedata.name(c)
    
# ==============================================================================
# ==============================================================================
# ==============================================================================    

# The category codes are abbreviations describing the nature of the character.
# These are grouped into categories such as “Letter”, “Number”, “Punctuation”, or “Symbol”, 
# To take the codes from the above output, 'Ll' means ‘Letter, lowercase’, 
# 'No' means “Number, other”, 'Mn' is “Mark, nonspacing”



test_string = "mark allan hatcher"
for c in test_string:
    print(c)
 
# string leading and lagging characters......
test_string = "0000000this is string example....wow!!!0000000"
print test_string.strip( '0' )
 


str_uber_path = (r'/Volumes/ORANGE/Documents/Projects/BigData/'
                 r'Skills/Python/NLTK-2.0/data_camp/chapter_2/'
                 r'uber_article.txt')


import codecs
f = codecs.open(str_uber_path, 'r', encoding = 'utf-8')
for line in f:
    # this takes out blank lines
    line = line.strip()  
    # this prints the u\2019 characters
    #print line.encode('unicode_escape')
    # this does not print the u\2019 characters
    print line
f.close()
 


import nltk 
f = codecs.open(str_uber_path, 'r', encoding = 'utf-8')
uber_article = f.read()
print(uber_article)
sentences = nltk.sent_tokenize(uber_article)



def fn_check_char(str_input):
    bln_res = False
    for char in str_input:
        if ord(char) > 127:
            bln_res = True
        break
    return bln_res


# when you declare a string with a u in front it tells Python that this
# is unicode not bytes...... 
str_u_code_test_a = 'I can eat おはss  glass よう here'
str_u_code_test_u = u'I can eat おはss  glass よう here'

# normal version.....
for x in str_u_code_test_a:
    print(x + ' ' + str(ord(x))) 

# unicode version...
for x in str_u_code_test_u:
    print(x + ' ' + str(ord(x))) 

from nltk.tokenize import word_tokenize
lst_tokens = word_tokenize(str_u_code_test_u)

lst_boolean = []
for word in lst_tokens:
    lst_boolean.append(fn_check_char(word))
    
for word, bln_is_word in zip(lst_tokens, lst_boolean):
    print(word + " " + str(bln_is_word))




