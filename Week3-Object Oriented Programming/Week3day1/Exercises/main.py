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
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway = Song(["There’s a lady who's sure",
#                  "all that glitters is gold",
#                  "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo!")
        else:
            print(f"{new_animal} is already in the zoo!")
    
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from the zoo.")
        else:
            print(f"{animal_sold} is not in the zoo!")
    
    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]
        return sorted_animals
    
    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Animals grouped by first letter:")
        for key, value in sorted_animals.items():
            print(f"{key}: {value}")

ramat_gan_safari = Zoo("Ramat Gan Safari")

# Call the methods
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Tiger")
ramat_gan_safari.get_animals()
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
