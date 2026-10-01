# Functions package reusable behavior into named blocks.
# Define with def, accept parameters, and return a result.

def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


def rectangle_area(width, height):
    return width * height


print(greet("Ada"))
print(rectangle_area(4, 5))

# A function can return multiple values as a tuple.
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

quotient, remainder = divide_with_remainder(17, 5)
print(quotient, remainder)

# Keep functions focused on one responsibility.
def is_positive(number):
    return number > 0

print(is_positive(3))
