"""
search.py

This file searches through the dataset and finds
the most similar sentences to the user's query.
"""

from data import sentences
from embed import get_embeddings
from similarity import cosine_similarity


def search(query, top_k=3):
    """
    Search for the most similar sentences.
    """

    # Add the query as the last sentence
    all_sentences = sentences + [query]

    # Convert every sentence into a vector
    vectors, vocabulary = get_embeddings(all_sentences)

    # The last vector belongs to the query
    query_vector = vectors[-1]

    # Remaining vectors belong to the dataset
    sentence_vectors = vectors[:-1]

    scores = []

    # Compare the query with every sentence
    for i, vec in enumerate(sentence_vectors):

        score = cosine_similarity(query_vector, vec)

        scores.append((sentences[i], score))

    # Sort from highest similarity to lowest
    scores.sort(key=lambda x: x[1], reverse=True)

    # Return the top matches
    return scores[:top_k]


if __name__ == "__main__":

    print("=" * 60)
    print("VECTOR SIMILARITY SEARCH")
    print("=" * 60)

    query = input("\nEnter your search query: ")

    results = search(query)

    print("\nTop Matches:\n")

    for sentence, score in results:
        print(f"Similarity: {score:.4f}")
        print(f"Sentence  : {sentence}")
        print("-" * 60)