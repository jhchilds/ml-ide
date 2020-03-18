from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
import json
import numpy as np

data_list = json.load(open("data.json"))
corpus = [data["data"] for data in data_list]
target = [target["target"] for target in data_list]

vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 2), max_features=100)
vectorized_X = vectorizer.fit_transform(corpus)

X = vectorized_X.toarray()

target = np.asarray(target)
target = target.reshape((len(target), 1)) # column vector
data_with_labels = np.append(X, target, axis=1)

balanced_X = np.zeros((1000, 100))
balanced_y = np.zeros(1000, dtype="str")

counts = {}

index = 0
for row in data_with_labels:
    label = row[-1]
    if label in counts:
        counts[label] += 1
    else:
        counts[label] = 1

    if counts[label] <= 500:
        balanced_X[index] = row[:-1]
        balanced_y[index] = row[-1]
        index += 1

print(counts)
print(balanced_X)

standardized_X = preprocessing.scale(balanced_X)

np.save("vectorized_X", standardized_X)
np.save("vectorized_y", balanced_y)