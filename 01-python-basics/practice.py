# Practice exercises for operators, conditions, loops, and I/O.

# 1. Return True when a number is even.
def is_even(number):
    return number % 2 == 0

# 2. Return the largest value without using max().
def largest(first, second, third):
    result = first
    if second > result:
        result = second
    if third > result:
        result = third
    return result

# 3. Return the sum of numbers from 1 through limit.
def sum_to(limit):
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total

# 4. Count how many times a value occurs in a list.
def count_value(values, target):
    count = 0
    for value in values:
        if value == target:
            count += 1
    return count

print(is_even(8))
print(largest(4, 9, 2))
print(sum_to(5))
print(count_value(["a", "b", "a", "a", "b", "a"], "a"))
