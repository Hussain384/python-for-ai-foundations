"""Portable paths and directory operations with pathlib."""

from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory(prefix="phase04-paths-") as temporary_directory:
    # __file__ anchors paths to this script, not to the shell's current directory.
    lesson_directory = Path(__file__).resolve().parent
    sample_directory = Path(temporary_directory) / "sample_data"
    sample_directory.mkdir()

    sample_file = sample_directory / "notes.txt"
    sample_file.write_text(
        "Python paths are objects, not string fragments.\n",
        encoding="utf-8",
    )

    print("Lesson directory:", lesson_directory)
    print("File name:", sample_file.name)
    print("Suffix:", sample_file.suffix)
    print("Parent:", sample_file.parent)
    print("Absolute path:", sample_file.resolve())
    print("Exists:", sample_file.exists())
    print("Is a file:", sample_file.is_file())
    print("Files in sample directory:")
    for path in sorted(sample_directory.iterdir()):
        if path.is_file():
            print(" -", path.name)

    # Glob patterns make it easy to find a group of files.
    print("Text files:", [path.name for path in sample_directory.glob("*.txt")])
