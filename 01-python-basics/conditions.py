# Conditions choose which block of code should run.

score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C or below"

print(grade)

# Conditions use truthy and falsy values.
items = ["Python"]
if items:
    print("The list has items")

# Use a guard clause to handle an invalid case early.
def describe_number(number):
    if number is None:
        return "No number provided"
    if number > 0:
        return "positive"
    if number < 0:
        return "negative"
    return "zero"

print(describe_number(-4))

# Conditional expressions are useful for short choices.
status = "adult" if score >= 18 else "minor"
print(status)
