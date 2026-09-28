# Python operators: symbols and keywords used to calculate and compare values.

first_number = 10
second_number = 3

# Arithmetic operators.
print(first_number + second_number)  # addition: 13
print(first_number - second_number)  # subtraction: 7
print(first_number * second_number)  # multiplication: 30
print(first_number / second_number)  # division: 3.333...
print(first_number // second_number) # floor division: 3
print(first_number % second_number)  # remainder: 1
print(first_number ** second_number) # exponentiation: 1000

# Comparison operators return True or False.
print(first_number > second_number)
print(first_number == second_number)
print(first_number != second_number)

# Logical operators combine conditions.
age = 25
has_id = True
print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)

# Membership and identity operators.
print("py" in "python")       # membership: True
print("x" not in "python")
value = None
print(value is None)            # identity check; preferred for None

# Assignment operators update a variable.
count = 5
count += 2
count *= 2
print(count)
