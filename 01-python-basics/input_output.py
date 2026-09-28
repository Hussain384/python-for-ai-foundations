# Input and output connect a program to its user or another system.

# print writes text to standard output.
name = "Ada"
score = 95
print("Name:", name)
print(f"{name} scored {score}%")  # f-strings embed expressions in text.

# input always returns a string. Convert it when numeric data is required.
def ask_for_age():
    response = input("Age: ")
    return int(response)

# Uncomment to run the interactive example:
# age = ask_for_age()
# print(f"Next year you will be {age + 1}.")

# Files should be opened with a context manager so they close automatically.
#
# open(path, mode, encoding) returns a file object:
# - path: the file name or path; relative paths start from the current folder.
# - "w": write mode; creates the file or replaces its existing contents.
# - encoding="utf-8": converts Python text to bytes consistently.
def save_message(path, message):
    # with calls file.close() automatically when this indented block ends,
    # including when an exception occurs. This releases the OS file handle.
    with open(path, "w", encoding="utf-8") as file:
        file.write(message)

# Other useful modes: "r" reads, "a" appends, and "x" creates only if absent.
# Use save_message("message.txt", "Hello") to write a file.

# Debugging means inspecting state and following an error to its source.
debug_value = "line\n"
print(debug_value)       # Displays the newline as an actual line break.
print(repr(debug_value)) # Displays the exact representation: 'line\n'.

# A traceback shows the exception type, message, and the line that failed.
# Example: int("abc") raises ValueError because "abc" is not a number.

# Put a breakpoint where you want execution to pause in a debugger.
# breakpoint()  # inspect variables, then continue or step through the code

# assert checks an assumption during development.
assert isinstance(score, int), "score must be an integer"
