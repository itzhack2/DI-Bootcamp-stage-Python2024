import re
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        word_count = Counter(self.text.split())
        return word_count.get(word, "Word not found")

    def most_common_word(self):
        words = re.findall(r'\w+', self.text.lower())
        word_count = Counter(words)
        return max(word_count, key=word_count.get)

    def unique_words(self):
        words = re.findall(r'\w+', self.text.lower())
        return list(set(words))

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)


class TextModification(Text):
    def remove_punctuation(self):
        return re.sub(r'[^\w\s]', '', self.text)

    def remove_stopwords(self):
        stopwords = set(['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'by', 'of', 'in', 'with'])
        words = re.findall(r'\w+', self.text.lower())
        return ' '.join(word for word in words if word not in stopwords)

    def remove_special_characters(self):
        return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)


# Part I - Analyzing simple string
simple_text = "A good book would sometimes cost as much as a good house."
simple_text_analysis = Text(simple_text)

print("Word frequency of 'good':", simple_text_analysis.word_frequency('good'))
print("Most common word:", simple_text_analysis.most_common_word())
print("Unique words:", simple_text_analysis.unique_words())

# Part II - Analyzing text from file
stranger_text_analysis = Text.from_file('the_stranger.txt')

print("\nMost common word in 'The Stranger':", stranger_text_analysis.most_common_word())
print("Unique words in 'The Stranger':", stranger_text_analysis.unique_words())

# Bonus - Text modification
modified_stranger_text = TextModification.from_file('the_stranger.txt')

print("\nText without punctuation:\n", modified_stranger_text.remove_punctuation())
print("\nText without stopwords:\n", modified_stranger_text.remove_stopwords())
print("\nText without special characters:\n", modified_stranger_text.remove_special_characters())
