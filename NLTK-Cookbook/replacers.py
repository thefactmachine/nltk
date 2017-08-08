import re
import enchant
from nltk.metrics import edit_distance




#define a list of tuples

# 'w' this is a word character such as: letters, digits and underscores.
replacement_patterns = [
  (r'won\'t', 'will not'),
  (r'can\'t', 'cannot'),
  (r'i\'m', 'i am'),
  (r'ain\'t', 'is not'),
  (r'(\w+)\'ll', '\g<1> will'),
  (r'(\w+)n\'t', '\g<1> not'),
  (r'(\w+)\'ve', '\g<1> have'),
  (r'(\w+)\'s', '\g<1> is'),
  (r'(\w+)\'re', '\g<1> are'),
  (r'(\w+)\'d', '\g<1> would')

]

class RegexpReplacer(object):

  #__init__ is run when class is instanciated
  def __init__(self, patterns=replacement_patterns):

    #this just compiles the replacement_patterns above
    self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

  def replace(self, text):
    s = text
    #iterate throught the list 'replacement_patterns'  
    for (pattern, repl) in self.patterns:
      #look in 's' for 'pattern' and replace with 'repl'
      #rs.subn is like re.sub but returns a tuple with count for the number of matches obtained.
      (s, count) = re.subn(pattern, repl, s)
    return s


class RepeatReplacer(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'

    
    def replace(self, word):
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
          return self.replace(repl_word)

        else:
          return repl_word


        
class SpellingReplacer(object):

  def __init__(self, dict_name='en', max_dist=2):
    self.spell_dict = enchant.Dict(dict_name)
    self.max_dist=2

  def replace(self, word):
    if self.spell_dict.check(word):
      return(word)

    suggestions = self.spell_dict.suggest(word)

    if suggestions and edit_distance(word, suggestions[0]) <= self.max_dist:
      return suggestions[0]
    else:
      return word



class wordReplacer(object):

  def __init__(self, word_map):
    self.word_map = word_map

  def replace(self, word):
    return self.word_map.get(word, word)
    

import csv
class CsvWordReplacer(wordReplacer):
  def __init__(self, fname):
    word_map = {}
    for line in csv.reader(open(fname)):
      word, syn = line
      word_map[word] = syn
    super(CsvWordReplacer, self).__init__(word_map)


    
from nltk.corpus import wordnet

class AntonymReplacer(object):
  def replace(self, word, pos=None):
    antonyms = set()
    for syn in wordnet.synsets(word, pos=pos):
      for lemma in syn.lemmas:
        for antonym in lemma.antonyms():
          antonyms.add(antonym.name)
    if len(antonyms) == 1:              #only return antonym if unambiguous
      return antonyms.pop()             #returns and removes element
    else:
      return None                       #if no antonyms or many antonyms return null
  

  def replace_negations(self, sent):
    i, l = 0, len(sent)                 #l is length of list
    words = []
    while i < l:                        #iterate through sent list
      word = sent[i]                    # word is sent list element
      if word == 'not' and i+1 < l:     #"not","nextword" exists("netword") true  
        ant = self.replace(sent[i+1])   # get antonym(nextword)
        if ant:                         # check if we could actually geta an antonym
          words.append(ant)             # append antonym to words list
          i += 2                        # skip to next potential "not"
          continue                      # returns to beggining of while
      words.append(word)                # append to word list
      i += 1                            #increment i
    return words                        #return list of words
    




      



    




 
    

  







