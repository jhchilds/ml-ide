import numpy as np


X = np.memmap("attempt1/vectorized_X.npy", dtype="uint16", mode="r", shape=(10000000, 500))
