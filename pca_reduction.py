import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA

data = np.load("vectorized.npy")
print(data)
print(data.shape)
balanced_X = np.zeros((1000, 100))
balanced_y = np.zeros(1000, dtype="str")

counts = {}
index = 0

for row in data:
    label = row[-1]
    if label in counts:
        counts[label] += 1
    else:
        counts[label] = 1

    if counts[label] <= 500:
        balanced_X[index] = row[:-1]
        balanced_y[index] = row[-1]
        index += 1

standardized_X = preprocessing.scale(balanced_X)

pca = PCA(n_components=3)
X_new = pca.fit_transform(standardized_X)

print(pca.explained_variance_ratio_)
print(X_new)