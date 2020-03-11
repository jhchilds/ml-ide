from gensim.test.utils import common_texts
from gensim.sklearn_api import W2VTransformer
# Create a model to represent each word by a 10 dimensional vector.
model = W2VTransformer(size=2, min_count=1, seed=1)

print(common_texts)

# What is the vector representation of the word 'graph'?
wordvecs = model.fit(common_texts).transform(['human', 'interface', 'trees'])
print(wordvecs)
