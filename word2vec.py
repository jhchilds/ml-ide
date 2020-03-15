from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer


corpus = []
for path in Path('./repos-cloned').rglob('*.py'):
    f = open("./" + str(path), "r")
    corpus.append(f.read())

vectorizer = CountVectorizer(analyzer='char', ngram_range=(1,1)) # can be Word or Char
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(X.toarray())



