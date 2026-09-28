# Tuples are ordered, immutable collections.
# Use a tuple for fixed data that should not be changed accidentally.

point = (10, 20)
user_record = ("Ada", "ada@example.com", True)

# Indexing and unpacking work like lists.
print(point[0])
print(point[0:1])    # slicing returns a new tuple: (10,)
x_coordinate, y_coordinate = point
print(x_coordinate, y_coordinate)

for coordinate in point:
    print(coordinate)

# A one-item tuple needs a trailing comma.
single_item = ("Python",)
print(single_item)

# Tuples support count and index, but not append or item assignment.
coordinates = (10, 20, 10)
print(coordinates.count(10))
print(coordinates.index(20))

# Tuples are useful for returning multiple values.
def min_max(values):
    return min(values), max(values)

lowest, highest = min_max([4, 1, 9])
print(lowest, highest)
