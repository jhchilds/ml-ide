import pickle
import numpy as np

y = pickle.load(open("attempt2/vectorized_y.pickle", "rb"))

y = np.asarray(y)
# y = y.reshape((len(y), 1))

target_counts = {}
for label in y:
    if label not in target_counts:
        target_counts[label] = 0
    target_counts[label] += 1
print(target_counts)

print(y.shape)
