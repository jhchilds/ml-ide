import pickle
import numpy as np
from scipy import sparse

ATTEMPT = "attempt3"

X = sparse.load_npz(f"{ATTEMPT}/vectorized_X.npz")
print("loaded")

X = X.toarray()
print("to array")

X = X.astype("uint16")
print("as uint16")

np.save(f"{ATTEMPT}/vectorized_X", X)
