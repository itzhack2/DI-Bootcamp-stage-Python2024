from anagram_checker import AnagramChecker

def get_input_word():
    while True:
        word = input("Enter a word (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            return None
        if len(word.split()) > 1:
            print("Error: Only one word is allowed.")
            continue
        if not word.isalpha():
            print("Error: Only alphabetic characters are allowed.")
            continue
        return word.strip()

def main():
    print("Welcome to the Anagram Checker!")
    word_list_file = "list.txt"  
    anagram_checker = AnagramChecker(word_list_file)
    
    while True:
        word = get_input_word()
        if not word:
            print("Exiting...")
            break
        if anagram_checker.is_valid_word(word):
            anagrams = anagram_checker.get_anagrams(word)
            print(f"\nYOUR WORD: \"{word}\"")
            print("This is a valid English word.")
            print("Anagrams for your word:", ', '.join(anagrams) if anagrams else "None")
        else:
            print("Sorry, the word you entered is not a valid English word.")

if __name__ == "__main__":
    main()
