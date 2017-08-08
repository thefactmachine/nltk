
text = open('theroartext.txt','r').read()
#load PunktSentenceTokeniser from pickle and call its tokenize() method
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
lstSentences = tokenizer.tokenize(text)
print(lstSentences)


