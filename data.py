"""
data.py

This file contains the text dataset that our vector search engine
will search through.

"""

sentences = [

    # ======================
    # Technology
    # ======================
    "Python is one of the most popular programming languages.",
    "Machine learning helps computers learn from data.",
    "Artificial intelligence is transforming many industries.",
    "Data science combines statistics and programming.",
    "Git is used to manage software projects.",

    # ======================
    # Food
    # ======================
    "Pizza is my favorite weekend meal.",
    "Pasta with white sauce tastes delicious.",
    "Chocolate ice cream is my favorite dessert.",
    "Fresh fruits are important for good health.",
    "Coffee helps many people stay productive.",

    # ======================
    # Sports
    # ======================
    "Football is the world's most popular sport.",
    "Cricket is loved by millions in India.",
    "Regular exercise improves physical health.",
    "Running every morning builds endurance.",
    "Swimming is a full body workout.",

    # ======================
    # Finance
    # ======================
    "Investing in stocks can build long-term wealth.",
    "Saving money is an important financial habit.",
    "Cryptocurrency prices are highly volatile.",
    "Mutual funds reduce investment risk.",
    "Financial planning helps achieve future goals.",

    # ======================
    # Animals
    # ======================
    "Dogs are loyal and friendly pets.",
    "Cats enjoy sleeping in sunny places.",
    "Elephants are the largest land animals.",
    "Birds migrate during different seasons.",
    "Dolphins are highly intelligent mammals.",

    # ======================
    # Education
    # ======================
    "Students should practice coding every day.",
    "Mathematics is the foundation of machine learning.",
    "Reading books improves vocabulary.",
    "Online courses make learning accessible.",
    "Consistency is the key to mastering new skills."

]

if __name__ == "__main__":
    print(f"Total Sentences: {len(sentences)}\n")

    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")