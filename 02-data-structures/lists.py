# Lists are ordered, mutable collections that allow duplicate values.
# Use a list when the sequence may change or when order matters.

numbers = [10, 20, 30, 20]

# Indexing and slicing.
print(numbers[0])       # first item: 10
print(numbers[-1])      # last item: 20
print(numbers[1:3])     # slice: [20, 30]

# Mutating a list.
numbers.append(40)       # add one item at the end
numbers.extend([50, 60]) # add multiple items
numbers.insert(1, 15)    # add at an index
numbers.remove(20)       # remove the first matching value
last_number = numbers.pop()  # remove and return the last item

print(numbers)
print(last_number)

# Useful operations.
print(len(numbers))
print(30 in numbers)
numbers.sort()
print(numbers)

# Copy the values before changing the copy independently.
copy_of_numbers = numbers.copy()
copy_of_numbers.append(100)
print(numbers)
print(copy_of_numbers)
