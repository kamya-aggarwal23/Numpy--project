# Vector Similarity Search

This project is a simple vector similarity search engine built using **Python** and **NumPy**. The main goal was to understand how text can be converted into vectors and how similar documents can be retrieved using cosine similarity.

## Features

- Text preprocessing (lowercase, punctuation removal)
- Vocabulary creation
- Bag of Words vector generation
- Cosine Similarity calculation
- Search for the most similar sentences

## Project Structure

```
vector-similarity-search/
│── data.py
│── embed.py
│── similarity.py
│── search.py
│── README.md
```

## How to Run

Clone the repository and run:

```bash
python search.py
```

Enter a query in the terminal to get the most similar sentences from the dataset.

## Example

Query:

```
machine learning
```

Output:

```
Similarity: 0.81
Machine learning helps computers learn from data.
```

## What I Learned

While building this project I learned:

- Text preprocessing
- Bag of Words representation
- Vector similarity
- Cosine Similarity
- Basic information retrieval using Python and NumPy

## Future Improvements

- Implement TF-IDF from scratch
- Compare results with Scikit-learn
- Use Sentence Transformers for semantic search