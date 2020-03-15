from sklearn.feature_extraction.text import CountVectorizer
import json
import numpy as np

data_list = json.load(open("data.json"))
corpus = [data["data"] for data in data_list]
target = [target["target"] for target in data_list]

vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 2), max_features=1000)
vectorized_X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
features = vectorized_X.toarray()
target = np.asarray(target)
target = target.reshape((len(target), 1))

X = np.append(features, target, axis=1)
print(X)
np.save("vectorized", X)

