def sort_words(words):
    """Sort words alphabetically and return as a comma-separated sequence."""
    sorted_words = sorted(words.split(','))
    return ','.join(sorted_words)

input_words = "without,hello,bag,world"
print(sort_words(input_words))  

def longest_word(sentence):
    """Find the longest word in a sentence."""
    words = sentence.split()
    longest = max(words, key=len)
    return longest.strip(".,?!")


sentence1 = "Margaret's toy is a pretty doll."
sentence2 = "A thing of beauty is a joy forever."
sentence3 = "Forgetfulness is by all means powerless!"

print(longest_word(sentence1))  
print(longest_word(sentence2))  
print(longest_word(sentence3))  
