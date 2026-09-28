# Loops repeat work over an iterable or while a condition is true.

# for is the usual choice when iterating over a collection or range.
languages = ["Python", "SQL", "JavaScript"]
for language in languages:
    print(language)

for number in range(1, 4):
    print(number)

# enumerate provides both the index and the value.
for index, language in enumerate(languages, start=1):
    print(index, language)

# Use break to stop and continue to skip the current iteration.
for number in range(6):
    if number == 2:
        continue
    if number == 5:
        break
    print(number)

# while repeats until its condition becomes false.
remaining = 3
while remaining > 0:
    print(remaining)
    remaining -= 1

# Comprehensions create collections concisely.
squares = [number * number for number in range(5)]
print(squares)
