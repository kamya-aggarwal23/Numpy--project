"""
embed.py

This file is responsible for converting raw text into a format
that the computer can understand.

Step 1:
Build a vocabulary from all the sentences.
"""

import string
from data import sentences


def preprocess_text(text):
    """
    Convert text to lowercase, remove punctuation,
    and split it into individual words.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    return words


def build_vocabulary(sentences):
    """
    Build a list of all unique words in the dataset.
    """

    vocabulary = []

    for sentence in sentences:

        words = preprocess_text(sentence)

        for word in words:

            if word not in vocabulary:
                vocabulary.append(word)

    return vocabulary

def sentence_to_vector(sentence, vocabulary):
    """
    Convert a sentence into a Bag of Words vector.

    """

    words = preprocess_text(sentence)

    vector = []

    for vocab_word in vocabulary:
        count = 0

        for word in words:
            if word == vocab_word:
                count += 1

        vector.append(count)

    return vector


def build_document_vectors(sentences, vocabulary):
    """
    Convert every sentence in the dataset into a vector.
    """

    document_vectors = []

    for sentence in sentences:
        vector = sentence_to_vector(sentence, vocabulary)
        document_vectors.append(vector)

    return document_vectors

def get_embeddings(sentences):
    """
    Build the vocabulary and convert all sentences
    into their Bag of Words vectors.
    """

    vocabulary = build_vocabulary(sentences)

    vectors = build_document_vectors(sentences, vocabulary)

    return vectors, vocabulary

if __name__ == "__main__":

    vocabulary = build_vocabulary(sentences)

    print("=" * 60)
    print("VOCABULARY")
    print("=" * 60)

    print(vocabulary)

    print("\n")

    vectors = build_document_vectors(sentences, vocabulary)

    print("=" * 60)
    print("FIRST SENTENCE")
    print("=" * 60)

    print(sentences[0])

    print("\nVector:\n")

    print(vectors[0])