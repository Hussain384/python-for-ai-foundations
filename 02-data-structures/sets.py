# Sets are unordered collections of unique, hashable values.
# Use a set for uniqueness, membership tests, and set operations.

numbers = {1, 2, 2, 3}
print(numbers)  # duplicate 2 is stored once

# Build a set from another iterable with set().
letters = set("banana")
print(letters)

# Add and remove values.
letters.add("x")
letters.discard("z")  # safe when the value may be missing
print(letters)

# Set operations compare groups of values.
backend = {"Python", "SQL", "Docker"}
data_tools = {"Python", "SQL", "Pandas"}
print(backend | data_tools)  # union: values in either set
print(backend & data_tools)  # intersection: values in both sets
print(backend - data_tools)  # difference: only in backend
print(backend ^ data_tools)  # symmetric difference: in one, not both

# Membership is a common and fast set operation.
print("Python" in backend)
