# # 🌟 Exercise 1: Cats
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat("Whiskers", 5)
# cat2 = Cat("Fluffy", 3)
# cat3 = Cat("Mittens", 7)

# def find_oldest_cat(*cats):
#     oldest_cat = max(cats, key=lambda cat: cat.age)
#     return oldest_cat

# oldest_cat = find_oldest_cat(cat1, cat2, cat3)
# print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")



# 🌟 Exercise 2 : Dogs
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         jump_height = self.height * 2
#         print(f"{self.name} jumps {jump_height} cm high!")


# davids_dog = Dog("Rex", 50)
# print(f"David's dog details - Name: {davids_dog.name}, Height: {davids_dog.height}")
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(f"Sarah's dog details - Name: {sarahs_dog.name}, Height: {sarahs_dog.height}")
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print(f"The bigger dog is {davids_dog.name}")
# elif davids_dog.height < sarahs_dog.height:
#     print(f"The bigger dog is {sarahs_dog.name}")
# else:
#     print("Both dogs are of the same height.")


# 🌟 Exercise 3 : Who’s The Song Producer?