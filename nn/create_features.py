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

ATTEMPT = "attempt3"


def get_labeled_source_of_type(type_):
    print(type_)
    paths = [(path, type_) for path in glob.glob(f"../repos-cloned/**/*.{type_}", recursive=True)]
    random.shuffle(paths)
    #paths = [("../repos-cloned/flask/src/flask/testing.py", "py")]
    print(len(paths))
    if len(paths) > 40000:
        paths = paths[:40000]
    return paths


file_paths = []
file_paths += get_labeled_source_of_type("py")
file_paths += get_labeled_source_of_type("c")
file_paths += get_labeled_source_of_type("js")
file_paths += get_labeled_source_of_type("java")
file_paths += get_labeled_source_of_type("swift")
file_paths += get_labeled_source_of_type("hs")
random.shuffle(file_paths)

chunk_length = 200

corpus = []
target = []
target_counts = {}
sample_index = 200
for file_tuple in file_paths:
    if file_tuple[1] not in target_counts:
        target_counts[file_tuple[1]] = 0
    if target_counts[file_tuple[1]] >= 100000:
        continue
    try:
        text = open(file_tuple[0]).read()

        if chunk_length:
            last_chunk_end = 0
            next_chunk_end = chunk_length
            while next_chunk_end < len(text):
                while next_chunk_end < len(text) and text[next_chunk_end] != "\n" and text[next_chunk_end] != ";":
                    next_chunk_end += 1
                chunk = text[last_chunk_end:next_chunk_end]
                corpus.append(chunk)
                target.append(file_tuple[1])
                target_counts[file_tuple[1]] += 1

                sample_index -= 1
                if sample_index <= 0:
                    sample_index = 200
                    print(file_tuple[0])
                    print("CHUNK:")
                    print(file_tuple[1])
                    print(chunk)

                last_chunk_end = next_chunk_end
                next_chunk_end += chunk_length
                target_counts[file_tuple[1]] += 1

            corpus.append(text[last_chunk_end:])
            target.append(file_tuple[1])
        else:
            corpus.append(text)
            target.append(file_tuple[1])
            # print("CHUNK:")
            # print(text[last_chunk_end:])
    except:
        pass

vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 2), lowercase=False, max_features=2000)
vectorized_X = vectorizer.fit_transform(corpus)
print(vectorized_X.shape)
print(len(target))
print("fit")

pickle.dump(vectorizer, open(f"{ATTEMPT}/vectorizer.pickle", "wb"))
print("vectorizer save")

sparse.save_npz(f"{ATTEMPT}/vectorized_X", vectorized_X)

pickle.dump(target, open(f"{ATTEMPT}/vectorized_y.pickle", "wb"))

