# Python's core built-in data types.
# Use type(value) to inspect a value's concrete type.

integer_value = 42                 # int: whole numbers; arbitrary precision
float_value = 3.14                 # float: decimal numbers
string_value = "Python"            # str: immutable Unicode text
boolean_value = True                # bool: True or False
list_value = ["a", "b", "a"]
# list: ordered and mutable; allows duplicates.
# Use it for a sequence that may grow, shrink, or change.

tuple_value = (10, 20)
# tuple: ordered and immutable; allows duplicates.
# Use it for fixed data, coordinates, or returning multiple values.

set_value = {"a", "b"}
# set: unordered collection of unique values.
# Use it to remove duplicates or test membership quickly.

dictionary_value = {"lang": "Python", "version": 3}
# dict: mutable key-value mapping; keys must be unique and hashable.
# Use it to represent named data or look up a value by key.

# None is the singleton used for "no value" or "not set".
missing_value = None

# Important behavior:
# - Python is dynamically typed: a name can be rebound to another type.
# - Mutable: list, set, and dict can change in place.
# - Immutable: int, float, bool, str, tuple, and None cannot change in place.
# - Collections can be nested and can hold mixed types.
# - Use == for value equality and is for object identity (especially None).

print(type(integer_value).__name__)

