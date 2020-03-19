import numpy as np
import plotly.express as px
from sklearn.decomposition import KernelPCA

data = np.load("vectorized.npy")

X = data[:, :-1]
y = data[:, -1]

pca = KernelPCA(n_components=2, n_jobs=-1)
X_new = pca.fit_transform(X)

print(X_new)

# fig = px.scatter(X_new[:,0], X_new[:,1])
# fig.show()
