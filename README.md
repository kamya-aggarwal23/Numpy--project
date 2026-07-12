# Vector Similarity Search

This project is a simple vector similarity search engine built using **Python** and **NumPy**. The goal was to understand how text can be converted into vectors and how similar documents can be retrieved using cosine similarity.

## Features

- Text preprocessing (lowercase and punctuation removal)
- Vocabulary creation
- Bag of Words vector generation
- Cosine Similarity calculation
- Search for the most similar sentences

## Project Structure

- data.py
- embed.py
- similarity.py
- search.py
- README.md

## How to Run

Clone the repository and run `python search.py`.

Then enter a query in the terminal to find the most similar sentences from the dataset.

## Example

**Query:** machine learning

**Result:** Machine learning helps computers learn from data. (Similarity: 0.81)

## What I Learned

While building this project, I learned:

- Text preprocessing
- Bag of Words representation
- Vector similarity
- Cosine Similarity
- Basic information retrieval using Python and NumPy

## Future Improvements

- Implement TF-IDF from scratch
- Compare results with Scikit-learn
- Use Sentence Transformers for semantic search