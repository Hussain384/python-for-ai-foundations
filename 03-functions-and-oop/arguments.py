# Function arguments provide data to a function.

# Positional arguments match parameters by order.
def describe_user(name, role="developer"):
    return f"{name} is a {role}."

print(describe_user("Ada"))
print(describe_user("Grace", "researcher"))

# Keyword arguments match parameters by name and improve readability.
print(describe_user(role="engineer", name="Linus"))

# *args collects extra positional arguments into a tuple.
def total(*numbers):
    return sum(numbers)

print(total(2, 4, 6))

# **kwargs collects extra keyword arguments into a dictionary.
def show_settings(**settings):
    for key, value in settings.items():
        print(key, value)

show_settings(theme="dark", notifications=True)

# Avoid mutable defaults such as items=[]; create them inside the function.
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("Python"))
