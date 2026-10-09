"""Analyze a UTF-8 text file from the command line."""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


WORD_PATTERN = re.compile(r"\b[\w']+\b", flags=re.UNICODE)
SENTENCE_PATTERN = re.compile(r"[.!?]+(?:[\"')\]]*)")


def analyze_text(text: str, top_count: int = 10) -> dict:
    """Return basic, reproducible text statistics.

    Sentence counting is intentionally heuristic: abbreviations and languages
    without whitespace-delimited words need a dedicated NLP tokenizer.
    """
    words = WORD_PATTERN.findall(text.casefold())
    sentences = [part for part in SENTENCE_PATTERN.split(text) if part.strip()]
    counts = Counter(words)
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences),
        "most_common_words": counts.most_common(top_count),
        "average_word_length": (
            sum(map(len, words)) / len(words) if words else 0.0
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="path to a UTF-8 text file")
    parser.add_argument("--top", type=int, default=10, help="number of frequent words")
    args = parser.parse_args()

    if args.top < 0:
        parser.error("--top must be zero or greater")
    try:
        text = args.input.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.error(f"cannot read {args.input}: {error}")

    result = analyze_text(text, args.top)
    print(f"Characters: {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Sentences: {result['sentences']}")
    print(f"Average word length: {result['average_word_length']:.2f}")
    print("Most common words:")
    if result["most_common_words"]:
        for word, count in result["most_common_words"]:
            print(f"  {word}: {count}")
    else:
        print("  (no words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
