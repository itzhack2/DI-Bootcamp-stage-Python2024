# 🌟Exercise 1 : What Are You Learning ?
# def display_message():
#     print("I am learning Python programming in this course.")
# display_message()

#  🌟 Exercise 2: What’s Your Favorite Book ?
# def favorite_book(title):
#     print(f'One of my favorite books is {title}')
# favorite_book("Alice in Wonderland")

# 🌟 Exercise 3 : Some Geography
# def describe_city(city,country="Unknown"):
#     print(f'{city} is in {country}')
# describe_city("Reykjavik","Iceland")
# describe_city('adiss')

# 🌟Exercise 4 : Random
# import random
# def compare_numbers(user_number):
#     random_number = random.randint(1, 100)
#     if user_number == random_number:
#         print("Congratulations! You guessed the correct number.")
#     else:
#         print(f"Sorry, you didn't guess the correct number. The random number was {random_number}.")
#         print(f"You guessed {user_number}.")
# user_input = int(input("Enter a number between 1 and 100: "))
# compare_numbers(user_input)

# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# def make_shirt(size='large' ,text='i love python'):
#     print(f'The size of the shirt is {size} and the text is {text}')
# make_shirt()
# make_shirt('medium')
# make_shirt('small', 'Hello World!')
# make_shirt(text='Coding is fun!', size='extra large')

# 🌟 Exercise 6 : Magicians …
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians(magician_names):
#     for magician in magician_names:
#         print(magician)

# def make_great(magician_names):
#     for i in range(len(magician_names)):
#         magician_names[i] = magician_names[i] + " the Great"
# make_great(magician_names)
# show_magicians(magician_names)

# 🌟 Exercise 7 : Temperature Advice
# import random
# def get_random_temp(season):
#     if season == 'summer':
#         return random.randint(16, 40)
#     elif season == 'autumn' or season == 'fall':
#         return random.randint(-10, 23)
#     elif season == 'winter':
#         return random.randint(-10, 16)
#     elif season == 'spring':
#         return random.randint(0, 32)
#     else:
#         return "Invalid season"

# def main():
#     season = input("Enter the season (summer, autumn, winter, spring): ")
#     temp = get_random_temp(season)
#     print(f"The temperature right now is {temp} degrees Celsius.")

#     if temp < 0:
#         print("Brrr, that's freezing! Wear some extra layers today.")
#     elif 0 <= temp < 16:
#         print("Quite chilly! Don't forget your coat.")
#     elif 16 <= temp < 23:
#         print("Moderate weather. Enjoy!")
#     elif 24 <= temp < 32:
#         print("It's warm outside. Stay hydrated!")
#     elif 32 <= temp <= 40:
#         print("It's hot! Keep cool and stay indoors if possible.")
# main()

# 🌟 Exercise 8 : Star Wars Quiz