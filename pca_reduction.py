import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA

X = np.load("vectorized_X.npy")
y = np.load("vectorized_y.npy")

pca = PCA(n_components=3)
X_new = pca.fit_transform(X)

print(pca.explained_variance_ratio_)
print(X_new)