"""Type hints: labels for humans and tools. Python does NOT enforce them
(unlike TypeScript, there is no compile step; mypy checks them separately).
"""

from dataclasses import dataclass

name: str = "Ada"
scores: list[float] = [0.9, 0.8]
ages: dict[str, int] = {"Ada": 36}


def average(values: list[float]) -> float:  # parameter hints, then -> return type
    return sum(values) / len(values)


# `X | None` means "may be missing"
def find_user(user_id: int) -> str | None:
    return {1: "Ada"}.get(user_id)


user = find_user(2)
if user is not None:  # handle None before using the value
    print(user.upper())
else:
    print("no such user")


def greet(name: str, excited: bool = False) -> str:
    return f"Hello, {name}{'!' if excited else '.'}"


print(greet("Ada", excited=True))


@dataclass
class Prediction:
    label: str
    confidence: float


print(Prediction("spam", 0.93))

# Not enforced: this runs even though the hint says str.
print(greet(123))

# Tip: hint function signatures first; skip obvious local variables.
