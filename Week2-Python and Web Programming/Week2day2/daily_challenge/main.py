# Challenge 1:
def generate_multiples(number, length):
    multiples = []
    current_number = number
    for _ in range(length):
        multiples.append(current_number)
        current_number += number
    return multiples

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

result = generate_multiples(number, length)
print(result)

# Challenge 2:

def remove_duplicates(word):
    modified_word = ""
    previous_char = None
    for char in word:
        if char != previous_char:
            modified_word += char
        previous_char = char
    return modified_word

user_word = input("Enter a word: ")
result = remove_duplicates(user_word)
print("Modified word:", result)
