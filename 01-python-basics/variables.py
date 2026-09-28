# A variable is a name bound to an object. Assignment uses =.

item = "Apple"
Item = "Banana"  # Names are case-sensitive: item != Item.

# Valid names use letters, digits, and underscores, but cannot start with a digit.
# Prefer snake_case; do not shadow built-ins such as list, str, or id.
user_name = "Ada"

# Python is dynamically typed: the name can be rebound to another object.
value = 10
value = "ten"

# Multiple assignment and unpacking.
x, y = 1, 2
first, second = ["a", "b"]
x, y = y, x  # swap without a temporary variable

# Constants are a convention, not enforced by Python.
MAX_RETRIES = 3

# == compares values; is compares object identity.
if item == "Apple":
	print(item)

# Use is None for a None check.
result = None
if result is None:
	print("No result")