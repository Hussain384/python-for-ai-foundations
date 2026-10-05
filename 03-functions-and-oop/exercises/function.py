# Practice: build reusable functions with parameters and return values.


def summarize_numbers(numbers):
    """Return the count, total, and average for a list of numbers."""
    count = len(numbers)
    total = sum(numbers)
    smallest = min(numbers)
    largest = max(numbers)
    average = total / count if count else 0
    return count, total, average, smallest, largest


def format_user(name, role="learner", **details):
    """Return a short description of a user."""
    detail_str = ", ".join(f"{key}: {value}" for key, value in details.items())
    return f"{name} is a {role} with details: {detail_str}"


def total_scores(*scores):
    """Return the average of any number of scores."""
    total = sum(scores)
    count = len(scores)
    return total / count if count else 0


numbers = [12, 18, 15, 20]
count, total, average, smallest, largest = summarize_numbers(numbers)
print("Summary:>", "Count:", count, "Total:", total, "Average:", average, "Smallest:", smallest, "Largest:", largest)
print(format_user("Ada", role="developer", location="NYC", experience="5 years"))
print(format_user("Grace", role="researcher", field="AI"))
print("Average score:", total_scores(8, 9, 10))

