"""Testing basics: call code with known input and check the result.

Run this file directly. In real projects tests go in tests/test_*.py and are run by pytest.
"""


def normalize_label(label):
    return " ".join(label.split()).lower()


def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b


# assert: crashes with AssertionError if the claim is false
assert normalize_label("  Positive ") == "positive"
assert normalize_label("VERY   Good") == "very good"
assert normalize_label("") == ""  # edge case: empty input

# test an expected error
try:
    safe_divide(1, 0)
except ZeroDivisionError:
    pass
else:
    raise AssertionError("expected ZeroDivisionError")

# floats: compare with a tolerance, never ==
assert abs((0.1 + 0.2) - 0.3) < 1e-9

print("all checks passed")

# The same tests in pytest (tests/test_labels.py) are just functions:
#
#   import pytest
#
#   def test_normalize_label():
#       assert normalize_label("  Positive ") == "positive"
#
#   def test_safe_divide_by_zero():
#       with pytest.raises(ZeroDivisionError):
#           safe_divide(1, 0)
#
# Run with:  python -m pytest
# Good tests: one behavior each, named for what they check, covering
# normal input, edge cases (empty, None) and expected errors.
