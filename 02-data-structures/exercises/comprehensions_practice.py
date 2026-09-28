# Practice: replace simple loops with comprehensions.

numbers = range(1, 11)
words = ["model", "data", "model", "token"]
records = [
    {"id": 1, "score": 0.91},
    {"id": 2, "score": 0.62},
    {"id": 3, "score": 0.84},
]

# TODO: create squares for even numbers only.
even_squares = [number * number for number in numbers if number % 2 == 0]

# TODO: create a set of unique lowercase words.
unique_words = {word.lower() for word in words}

# TODO: map record IDs to scores only for scores >= 0.8.
high_scores = {record["id"]: record["score"] for record in records if record["score"] >= 0.8}

print(even_squares)
print(unique_words)
print(high_scores)
