import numpy as np
import gensim.downloader as api 
import scipy.sparse as sp

# Load pre-trained word vectors
model = api.load('word2vec-google-news-300')

# Read in semantic lexicon
lexicon = {}
with open('ppdb-2.0-xl-all', 'r') as f:
    for line in f:
        fields = line.strip().split('\t')
        if len(fields) == 2:
            lexicon[(fields[0], fields[1])] = 1.0
        elif len(fields) == 3:
            lexicon[(fields[0], fields[1])] = float(fields[2])

# Compute cosine similarity between word vectors and lexicon
sims = {}
for word1, word2 in lexicon:
    if word1 in model.vocab and word2 in model.vocab:
        sims[(word1, word2)] = np.dot(model[word1], model[word2]) / (np.linalg.norm(model[word1]) * np.linalg.norm(model[word2]))

# Construct weighted graph
words = list(model.vocab.keys())
num_words = len(words)
A = sp.lil_matrix((num_words, num_words))
for i, word1 in enumerate(words):
    for j, word2 in enumerate(words):
        if (word1, word2) in sims:
            A[i, j] = sims[(word1, word2)]

# Compute Laplacian matrix
D = sp.spdiags(A.sum(axis=1).flatten(), [0], num_words, num_words)
L = D - A

# Solve linear equation for retrofitting weights
Y = np.zeros((num_words, model.vector_size))
for i, word in enumerate(words):
    if word in lexicon:
        Y[i] = model[word]
W = np.linalg.solve(L.todense() + np.eye(num_words), Y)

# Adjust original word vectors with retrofitting weights
for i, word in enumerate(words):
    model[word] += W[i]

