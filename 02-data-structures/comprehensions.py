# Comprehensions build collections from an iterable in one expression.
# Use them for simple transformations and filters; use a normal loop when logic is complex.

numbers = range(1, 6)

# List comprehension: transform every value.
squares = [number * number for number in numbers]
print(squares)

# Add a condition to filter values.
even_squares = [number * number for number in numbers if number % 2 == 0]
print(even_squares)

# Set comprehension keeps results unique.
initials = {name[0].upper() for name in ["Ada", "Alan", "Grace"]}
print(initials)

# Dictionary comprehension creates key-value pairs.
word_lengths = {word: len(word) for word in ["Python", "data", "model"]}
print(word_lengths)

# Nested comprehensions are possible, but readability matters.
coordinates = [(x, y) for x in range(2) for y in range(2)]
print(coordinates)
