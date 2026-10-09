"""Exercises: complete each task, then compare behavior with the lesson files."""

from pathlib import Path


def main():
    # 1. Build a path to "input.txt" beside this script using pathlib.
    input_path = Path(__file__).resolve().parent / "input.txt"

    # 2. Create the file's parent directory if it does not exist.
    input_path.parent.mkdir(parents=True, exist_ok=True)

    # 3. Write two UTF-8 lines, then read the file back using a context manager.
    input_path.write_text("First line.\nSecond line.\n", encoding="utf-8")
    with input_path.open("r", encoding="utf-8") as file:
        line_count = 0
        non_whitespace_count = 0
        for line in file:
            line_count += 1
            non_whitespace_count += sum(
                not character.isspace() for character in line
            )

    # 4. Print the number of lines and the number of non-whitespace characters.
    print("Lines:", line_count)
    print("Non-whitespace characters:", non_whitespace_count)

if __name__ == "__main__":
    main()
