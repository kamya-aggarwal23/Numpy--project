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


if __name__ == "__main__":

    vocabulary = build_vocabulary(sentences)

    print("=" * 60)
    print("VOCABULARY")
    print("=" * 60)

    print(f"\nTotal Unique Words: {len(vocabulary)}\n")

    for index, word in enumerate(vocabulary):
        print(f"{index:3} --> {word}")