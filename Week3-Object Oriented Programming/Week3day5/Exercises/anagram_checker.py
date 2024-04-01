class AnagramChecker:
    def __init__(self, word_list_file):
        with open(word_list_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file)

    def is_valid_word(self, word):
        return word.strip().isalpha() and word.strip().lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        return [w for w in self.word_list if self.is_anagram(word, w)]

from anagram_checker import AnagramChecker

def get_user_input():
    return input("Enter a word (or type 'exit' to quit): ").strip()

def display_anagrams(word, anagrams):
    print(f"Your word: \"{word.upper()}\"")
    if anagrams:
        print("This is a valid English word.")
        print("Anagrams for your word:", ", ".join(anagrams) + ".")
    else:
        print("This is not a valid English word or it has no anagrams.")

def main():
    anagram_checker = AnagramChecker("list.txt")
    
    while True:
        user_input = get_user_input()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        if ' ' in user_input:
            print("Error: Only a single word is allowed.")
            continue
        
        if not user_input.isalpha():
            print("Error: Only alphabetic characters are allowed.")
            continue
        
        word = user_input.strip().lower()
        
        if anagram_checker.is_valid_word(word):
            anagrams = anagram_checker.get_anagrams(word)
            display_anagrams(word, anagrams)
        else:
            print("Error: This is not a valid English word.")

if __name__ == "__main__":
    main()
