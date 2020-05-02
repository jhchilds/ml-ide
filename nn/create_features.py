import pandas as pd
import glob
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pickle


def get_labeled_source_of_type(type_):
    return [(path, type_) for path in glob.glob(f"../repos-cloned/**/*.{type_}", recursive=True)]


file_paths = []
file_paths += get_labeled_source_of_type("py")
file_paths += get_labeled_source_of_type("java")
file_paths += get_labeled_source_of_type("hs")

corpus = [open(file_path[0]).read() for file_path in file_paths]
target = [file_path[1] for file_path in file_paths]

vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 2), max_features=100)
vectorized_X = vectorizer.fit_transform(corpus)

pickle.dump(vectorizer, open("vectorizer.pickle", "wb"))

features = vectorized_X.toarray()

target = np.asarray(target)
target = target.reshape((len(target), 1))

np.save("vectorized_X", features)
np.save("vectorized_y", target)
