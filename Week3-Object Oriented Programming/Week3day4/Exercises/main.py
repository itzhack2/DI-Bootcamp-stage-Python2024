# 🌟 Exercise 1 – Random Sentence Generator
# import random
# def get_words_from_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             words = file.read().split()
#         return words
#     except FileNotFoundError:
#         print("Error: File not found.")
#         return []

# def get_random_sentence(words, length):
#     if length < 2 or length > 20:
#         raise ValueError("Length parameter should be between 2 and 20.")
#     random_words = random.sample(words, length)
#     return ' '.join(random_words).lower()

# def main():
#     print("This program generates a random sentence from a list of words in a file.")

#     while True:
#         try:
#             length = int(input("Enter the length of the sentence (between 2 and 20): "))
#             if 2 <= length <= 20:
#                 break
#             else:
#                 print("Error: Length should be between 2 and 20.")
#         except ValueError:
#             print("Error: Please enter a valid integer.")

#     words = get_words_from_file("words.txt")  # Change "words.txt" to your file path
#     if not words:
#         return

#     try:
#         sentence = get_random_sentence(words, length)
#         print("Random Sentence:", sentence)
#     except ValueError as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     main()

# 🌟 Exercise 2: Working With JSON
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# data = json.loads(sampleJson)

# salary = data["company"]["employee"]["payable"]["salary"]
# print("Salary:", salary)

# data["company"]["employee"]["birth_date"] = "1990-01-01"

# with open("modified_data.json", "w") as json_file:
#     json.dump(data, json_file, indent=4)

# print("JSON data saved to 'modified_data.json'.")
