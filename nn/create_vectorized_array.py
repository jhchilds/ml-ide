import pickle
import numpy as np
from scipy import sparse

X = sparse.load_npz("vectorized_X.npz")
print("loaded")

X = X.toarray()
print("to array")

X = X.astype("uint16")
print("as uint16")

np.save("vectorized_X", X)
