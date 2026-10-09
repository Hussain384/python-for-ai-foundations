# 04. Files and Data

## Paths and directories
- `pathlib.Path` represents file-system paths.
- `/` joins path parts in a platform-independent way.
- Useful properties and methods: `.name`, `.suffix`, `.parent`, `.resolve()`, `.exists()`, `.is_file()`, `.mkdir()`, `.iterdir()`, `.glob()`.
- `Path(__file__).resolve().parent` anchors a path to the script's directory.
- `TemporaryDirectory` is useful for examples and tests that should not leave files behind.

## Text files
- Specify an encoding when reading or writing; UTF-8 is a practical default.
- Use `Path.read_text()` / `Path.write_text()` for simple whole-file operations.
- Use `Path.open()` with a `with` statement for more control or line-by-line processing.
- A context manager closes the file even if an error occurs.
- Common modes: `"r"` read, `"w"` overwrite/create, `"a"` append, `"x"` create only if absent.
- Iterate over a file to process it one line at a time.

## JSON
- JSON objects map to Python dictionaries; arrays map to lists.
- JSON strings, numbers, booleans, and `null` map to Python strings, numbers, booleans, and `None`.
- `json.load()` / `json.dump()` read and write JSON files.
- `json.loads()` / `json.dumps()` convert JSON text without accessing files.
- Use `indent=2` for readable output and `ensure_ascii=False` to keep Unicode characters.
- Validate loaded data before assuming its shape or value types.

## CSV
- Use the standard-library `csv` module.
- `csv.DictReader` reads rows as dictionaries; `csv.DictWriter` writes dictionaries.
- Open CSV files with `newline=""` so the CSV module handles newlines correctly.
- Include a header row when writing with `writeheader()`.
- CSV cells are read as strings; convert numbers and booleans explicitly when needed.
- `encoding="utf-8-sig"` can handle CSV files that include a UTF-8 byte-order mark.

## Data-processing workflow
- Separate work into steps: load -> validate -> clean -> analyze -> save.
- `.strip()` removes leading and trailing whitespace; it does not remove spaces within text.
- Ignore or remove records only according to an explicit definition of "blank".
- Convert values carefully before calculating statistics.
- Check numeric values are finite before summarizing them.
- Keep the original input and write processed data to a separate output file.

## Command-line programs
- `argparse.ArgumentParser` defines and validates command-line arguments.
- Positional arguments are required unless defaults are provided.
- Optional arguments use flags, such as `--top 5`.
- `parser.error()` prints an error and exits with a nonzero status.
- Guard the entry point with `if __name__ == "__main__":`.

## Chapter projects
- `cli_text_analyzer.py` reads a UTF-8 text file and reports character, word, and sentence counts, average word length, and frequent words.
- `dataset_processor.py` reads JSON or CSV records, trims text, removes wholly blank records, writes a cleaned output file, and reports numeric-column statistics.
- Example, run from `04-files-and-data\projects`:

  ```powershell
  python cli_text_analyzer.py ..\sample_data\reading.txt --top 5
  python dataset_processor.py ..\sample_data\support_tickets.json ..\sample_data\support_tickets_processed.json
  ```

## Quick recall
- Use `Path` to build and inspect paths portably.
- Use UTF-8 and context managers for reliable file handling.
- JSON preserves structured types; CSV values start as text.
- Validate input and handle expected file and parsing errors.
- Save transformed data separately from the source.

## Practice checklist
- [ ] build paths with `pathlib`
- [ ] create and inspect directories
- [ ] read and write UTF-8 text files
- [ ] process files line by line
- [ ] serialize and deserialize JSON
- [ ] read and write CSV dictionaries
- [ ] convert CSV values to appropriate types
- [ ] validate and clean structured records
- [ ] add positional and optional CLI arguments
- [ ] run both chapter projects on sample files
