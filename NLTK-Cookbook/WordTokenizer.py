from nltk.tokenize import PunktWordTokenizer
tokenizer = PunktWordTokenizer()
strExSentence = "Can't is a contraction."
lstWordPunkt = tokenizer.tokenize(strExSentence)
print(lstWordPunkt)

#OUTPUT is ['Can', "'t", 'is', 'a', 'contraction.']


from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
lstWordPunkt = tokenizer.tokenize(strExSentence)
print(lstWordPunkt)

#OUTPUT is  ['Can', "'", 't', 'is', 'a', 'contraction', '.']


def fnTest(strArgument):
    print(strArgument)


fnTest("mark")




    
