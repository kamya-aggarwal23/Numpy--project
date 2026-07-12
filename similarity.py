import numpy as np


def cosine_similarity(vec1, vec2):
    """
    Calculate the cosine similarity between two vectors.

    Returns a value between -1 and 1:
        1  -> Exactly the same direction (most similar)
        0  -> Unrelated (perpendicular)
       -1  -> Completely opposite direction
    """

    # Step 1: Calculate the dot product.
    # This measures how much the two vectors point in the same direction.
    dot_product = np.dot(vec1, vec2)

    # Step 2: Find the length (magnitude) of each vector.
    # We need this so longer vectors don't automatically get larger scores.
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    # Step 3: Prevent division by zero.
    # If either vector has zero length, similarity cannot be calculated.
    if norm1 == 0 or norm2 == 0:
        return 0

    # Step 4: Apply the cosine similarity formula.
    similarity = dot_product / (norm1 * norm2)

    return similarity
if __name__ == "__main__":

    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])

    similarity = cosine_similarity(vector1, vector2)

    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print(f"Cosine Similarity: {similarity:.4f}")
