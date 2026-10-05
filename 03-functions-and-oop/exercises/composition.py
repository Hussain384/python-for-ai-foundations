# Practice: combine small objects into a larger workflow.


class TextCleaner:
    def clean(self, text):
        return " ".join(text.strip().split()).lower()


class KeywordFinder:
    def __init__(self, keywords):
        self.keywords = set(keyword.lower() for keyword in keywords)

    def find(self, text):
        words = set(text.split())
        return sorted(words.intersection(self.keywords))


class CharacterCounter:
    def count(self, text):
        return len(text)


class TextAnalyzer:
    def __init__(self, cleaner, keyword_finder, character_counter):
        self.cleaner = cleaner
        self.keyword_finder = keyword_finder
        self.character_counter = character_counter

    def analyze(self, text):
        cleaned_text = self.cleaner.clean(text)
        return {
            "text": cleaned_text,
            "word_count": len(cleaned_text.split()),
            "keywords": self.keyword_finder.find(cleaned_text),
            "character_count": self.character_counter.count(cleaned_text),
        }


analyzer = TextAnalyzer(
    TextCleaner(),
    KeywordFinder(["python", "ai", "data"]),
    CharacterCounter(),
)
print(analyzer.analyze("  Python helps build useful AI data tools.  "))
