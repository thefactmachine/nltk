from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
words = ["Can't", 'is', 'a', 'contraction']
lstFiltered = [word for word in words if word not in english_stops]
print(lstFiltered)
print(english_stops)
