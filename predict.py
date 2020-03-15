from sklearn.feature_extraction.text import CountVectorizer
import json
import numpy as np

data_list = json.load(open("data.json"))
corpus = [data["data"] for data in data_list]

vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 2), max_features=1000)
vectorized_X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(vectorized_X.toarray())

np.save("vectorized.np", vectorized_X.toarray())
