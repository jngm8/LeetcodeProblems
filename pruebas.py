import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Embedding, Input, Lambda
from tensorflow.keras.models import Model

# Define the maximum sentence length and embedding dimension
max_sentence_length = 50  # Adjust this according to your dataset
embedding_dim = 300  # Adjust this according to your word embeddings

# Example word embeddings for words in your vocabulary (replace this with your own)
word_embeddings = np.random.rand(10000, embedding_dim)
