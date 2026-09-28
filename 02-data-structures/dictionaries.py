# Dictionaries store key-value pairs.
# Use a dict for named data or fast lookup by a unique key.

user = {
    "name": "Ada",
    "role": "developer",
    "active": True,
}

# Read, add, update, and remove values.
print(user["name"])
print(user.get("timezone", "UTC"))  # default prevents a KeyError
user["role"] = "engineer"
user["team"] = "platform"
removed_role = user.pop("role")
print(user)
print(removed_role)

# Iterate over keys, values, or both.
for key, value in user.items():
    print(key, value)

# Check keys with in; dictionary keys are unique.
print("name" in user)
print(len(user))

# Nested dictionaries model structured records.
profile = {
    "name": "Ada",
    "contact": {"email": "ada@example.com", "verified": True},
}
print(profile["contact"]["email"])
