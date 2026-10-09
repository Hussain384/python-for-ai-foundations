"""Text-file I/O, encodings, and line-oriented processing."""

from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory(prefix="phase04-text-") as temporary_directory:
    sample_file = Path(temporary_directory) / "meeting_notes.txt"
    # Always specify an encoding. UTF-8 is a practical default for modern data.
    sample_file.write_text(
        "The first line contains Python.\n"
        "The second line mentions data and models.\n"
        "The final line is kept when this file is read.\n",
        encoding="utf-8",
    )

    complete_text = sample_file.read_text(encoding="utf-8")
    print("Whole file:")
    print(complete_text)

    # open() is useful when reading a file incrementally or writing multiple parts.
    # The context manager closes the file even if processing raises an exception.
    line_count = 0
    with sample_file.open("r", encoding="utf-8") as file:
        for line_count, line in enumerate(file, start=1):
            print(f"Line {line_count}: {line.rstrip()}")

    print("Line count:", line_count)

    # "a" appends; "w" replaces existing contents; "x" creates a new file only.
    with sample_file.open("a", encoding="utf-8") as file:
        file.write("Appended without reading the whole file first.\n")

    print("Updated size:", sample_file.stat().st_size, "bytes")
