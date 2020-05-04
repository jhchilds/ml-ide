import pandas as pd
import glob
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pickle
import logging
import random
from scipy import sparse

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')


def get_labeled_source_of_type(type_):
    print(type_)
    paths = [(path, type_) for path in glob.glob(f"../repos-cloned/**/*.{type_}", recursive=True)]
    random.shuffle(paths)
    #paths = [("../repos-cloned/flask/src/flask/testing.py", "py")]
    print(len(paths))
    if len(paths) > 20000:
        paths = paths[:20000]
    return paths


file_paths = []
file_paths += get_labeled_source_of_type("py")
file_paths += get_labeled_source_of_type("c")
file_paths += get_labeled_source_of_type("js")
file_paths += get_labeled_source_of_type("java")
file_paths += get_labeled_source_of_type("swift")
file_paths += get_labeled_source_of_type("hs")

chunk_length = 100

corpus = []
target = []
for file_tuple in file_paths:
    try:
        print(file_tuple[0])
        text = open(file_tuple[0]).read()

        last_chunk_end = 0
        next_chunk_end = chunk_length
        while next_chunk_end < len(text):
            while next_chunk_end < len(text) and text[next_chunk_end] != " ":
                next_chunk_end += 1
            chunk = text[last_chunk_end:next_chunk_end]
            corpus.append(chunk)
            target.append(file_tuple[1])
            # print("CHUNK:")
            # print(chunk)

            last_chunk_end = next_chunk_end
            next_chunk_end += chunk_length

        corpus.append(text[last_chunk_end:])
        target.append(file_tuple[1])
        # print("CHUNK:")
        # print(text[last_chunk_end:])
    except:
        pass

vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 4), lowercase=False, max_features=500)
vectorized_X = vectorizer.fit_transform(corpus)
print("fit")

pickle.dump(vectorizer, open("vectorizer.pickle", "wb"))
print("vectorizer save")

sparse.save_npz("vectorized_X", vectorized_X)

pickle.dump(target, open("vectorized_y", "wb"))

