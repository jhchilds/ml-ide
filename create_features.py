from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
import json
import numpy as np

data_list = json.load(open("data.json"))
corpus = [data["data"] for data in data_list]
target = [target["target"] for target in data_list]

vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 2), max_features=100)
vectorized_X = vectorizer.fit_transform(corpus)

features = vectorized_X.toarray()

target = np.asarray(target)
target = target.reshape((len(target), 1))  # column vector

data = np.append(features, target, axis=1)

np.save("vectorized", data)
