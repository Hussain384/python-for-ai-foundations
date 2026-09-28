# Practice: use indexing and slicing on sequences.

messages = [
    "Hello",
    "How can I help?",
    "Explain Python lists.",
    "Lists preserve order.",
]

# TODO: return the first and last message.
def first_and_last(items):
    return items[0], items[-1]

# TODO: return the middle section without changing the original list.
def middle_items(items):
    middle_start = 1
    middle_end = -1
    return items[middle_start:middle_end]

# TODO: return every second item.
def every_second(items):
    return items[::2]

print(first_and_last(messages))
print(middle_items(messages))
print(every_second(messages))
