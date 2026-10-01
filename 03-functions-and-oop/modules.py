# A module is a Python file that can be imported into another file.
# Imports let you reuse the standard library and your own code.

import math
from pathlib import Path
from text_utils import normalize_whitespace

print(math.sqrt(81))
print(math.pi)

# Path represents filesystem paths in a cross-platform way.
current_file = Path(__file__)
print(current_file.name)
print(current_file.suffix)

# Import only what you need when that improves clarity.
from datetime import date

print(date.today().year)

# Import reusable code from another module in this folder.
print(normalize_whitespace("  Python   for   AI  "))

# Protect executable code so the module can also be imported safely.
def square(number):
    return number * number


if __name__ == "__main__":
    print(square(6))
