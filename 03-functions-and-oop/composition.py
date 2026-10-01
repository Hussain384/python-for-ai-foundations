class TextNormalizer:
    def normalize(self, text):
        return " ".join(text.split()).lower()


class WordCounter:
    def count(self, text):
        return len(text.split())


class TextPipeline:
    def __init__(self, normalizer, word_counter):
        self.normalizer = normalizer
        self.word_counter = word_counter

    def analyze(self, text):
        normalized_text = self.normalizer.normalize(text)
        return {
            "text": normalized_text,
            "word_count": self.word_counter.count(normalized_text),
        }


pipeline = TextPipeline(TextNormalizer(), WordCounter())
print(pipeline.analyze("  Python   helps build       AI       projects.  "))