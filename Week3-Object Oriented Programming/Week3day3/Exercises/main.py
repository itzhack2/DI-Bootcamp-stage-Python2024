# # 🌟 Exercise 1: Currencies
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f"{self.amount} {self.currency}"
#     def __int__(self):
#         return self.amount
#     def __repr__(self):
#         return f"{self.amount} {self.currency}"
#     def __add__(self, other):
#         if isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             return Currency(self.currency, self.amount + other.amount)
#         else:
#             return Currency(self.currency, self.amount + other)

#     def __iadd__(self, other):
#         if isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             self.amount += other.amount
#             return self
#         else:
#             self.amount += other
#             return self
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))  # Output: '5 dollar'
# print(int(c1))  # Output: 5
# print(repr(c1))  # Output: '5 dollar'
# print(c1 + 5)   # Output: 10
# print(c1 + c2)  # Output: 15
# print(c1)       # Output: 5 dollar
# c1 += 5
# print(c1)       # Output: 10 dollar
# c1 += c2
# print(c1)       # Output: 20 dollar
# print(c1 + c3)  # Output: TypeError: Cannot add between Currency type <dollar> and <shekel>



# # 🌟 Exercise 3: String Module
# import random
# import string
# def generate_random_string(length):
#     characters = string.ascii_letters
#     return ''.join(random.choice(characters) for _ in range(length))
# random_string = generate_random_string(5)
# print(random_string)

# # 🌟 Exercise 4 : Current Date
# import datetime
# def display_current_date():
#     current_date = datetime.datetime.now().date()
#     print("Current date is:", current_date)
# display_current_date()

# #🌟 Exercise 5 : Amount Of Time Left Until January 1st
# import datetime
# def time_left_until_january_1st():
#     current_date = datetime.datetime.now()
#     january_1st_next_year = datetime.datetime(current_date.year + 1, 1, 1)
#     time_left = january_1st_next_year - current_date
   
#     days = time_left.days
#     hours, remainder = divmod(time_left.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     print("The 1st of January is in {} days and {}:{}:{} hours.".format(days, hours, minutes, seconds))
# time_left_until_january_1st()

# #🌟 Exercise 6 : Birthday And Minutes
# import datetime

# def minutes_lived(birthdate):
#     birthdate_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
#     current_date = datetime.datetime.now()
#     time_lived = current_date - birthdate_date
#     minutes = time_lived.total_seconds() / 60
#     print("You have lived for approximately {:.2f} minutes.".format(minutes))
# birthdate = "1990-05-15"
# minutes_lived(birthdate)

# Exercise 7 : Faker Module
# from faker import Faker

# faker = Faker()

# users = []

# def add_fake_user():
#     user = {
#         'name': faker.name(),
#         'address': faker.address(),
#         'language_code': faker.language_code()
#     }
#     users.append(user)
# for _ in range(5):
#     add_fake_user()
# print(users)
