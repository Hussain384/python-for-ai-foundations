# Practice: process documents, tokens, and configuration values.


def unique_words(documents):
    words = []
    for document in documents:
        words.extend(document.lower().split())
    return set(words)


def enabled_options(configuration):
    return [name for name, enabled in configuration.items() if enabled]


def token_count(messages):
    total = 0
    for message in messages:
        total += len(message["content"].split())
    return total


documents = ["Python is readable", "Python is useful"]
configuration = {"streaming": True, "debug": False, "cache": True}
messages = [
    {"role": "user", "content": "Explain lists"},
    {"role": "assistant", "content": "Lists are ordered collections"},
]

print(unique_words(documents))
print(enabled_options(configuration))
print(token_count(messages))
