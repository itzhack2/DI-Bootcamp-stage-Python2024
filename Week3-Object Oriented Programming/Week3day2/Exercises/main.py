# 🌟 Exercise 1 : Pets
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # Create instances of each cat breed
# bengal_cat = Bengal(name='BengalCat', age=3)
# chartreux_cat = Chartreux(name='ChartreuxCat', age=2)
# siamese_cat = Siamese(name='SiameseCat', age=1)

# # Create a list of all cats
# all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# # Create a Pets instance with all_cats as the parameter
# sara_pets = Pets(animals=all_cats)

# # Take all the cats for a walk
# sara_pets.walk()

# 🌟 Exercise 2 : Dogs
# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f'{self.name} is barking'

#     def run_speed(self):
#         return self.weight / self.age * 10

#     def fight(self, other_dog):
#         if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
#             return f'{self.name} won the fight against {other_dog.name}'
#         elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
#             return f'{other_dog.name} won the fight against {self.name}'
#         else:
#             return 'It was a tie!'

# # Create 3 dogs
# dog1 = Dog(name='Buddy', age=2, weight=20)
# dog2 = Dog(name='Max', age=3, weight=25)
# dog3 = Dog(name='Rocky', age=4, weight=22)

# # Test the methods
# print(dog1.bark())
# print(dog2.run_speed())
# print(dog3.fight(dog1))

# 🌟 Exercise 3 : Dogs Domesticated
# import random

# class PetDog(Dog):
#     def __init__(self, name, age, weight):
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self):
#         bark_output = super().bark()
#         print(bark_output)
#         self.trained = True

#     def play(self, *dog_names):
#         print(f'{", ".join(dog_names)} all play together')

#     def do_a_trick(self):
#         if self.trained:
#             trick_options = [
#                 f'{self.name} does a barrel roll',
#                 f'{self.name} stands on his back legs',
#                 f'{self.name} shakes your hand',
#                 f'{self.name} plays dead'
#             ]
#             print(random.choice(trick_options))
#         else:
#             print(f'{self.name} is not trained. Train the dog first.')

# # Example usage
# pet_dog = PetDog(name='Rover', age=2, weight=18)

# # Train the dog
# pet_dog.train()

# # Play with other dogs
# pet_dog.play('Buddy', 'Max', 'Rocky')

# # Do a trick
# pet_dog.do_a_trick()

# 🌟Exercise 4 : Family
# class Family:
#     def __init__(self, last_name, members):
#         self.last_name = last_name
#         self.members = members

#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print(f"Congratulations! {kwargs['name']} was born into the {self.last_name} family.")

#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name and member['age'] >= 18:
#                 return True
#         return False

#     def family_presentation(self):
#         print(f"Family Name: {self.last_name}")
#         for member in self.members:
#             print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

# # Initial members
# initial_members = [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ]

# # Create an instance of the Family class
# family_instance = Family(last_name='Smith', members=initial_members)

# # Call the methods
# family_instance.born(name='John', age=0, gender='Male', is_child=True)
# print(f"Is Sarah over 18? {family_instance.is_18('Sarah')}")
# family_instance.family_presentation()

# 🌟Exercise 5 : TheIncredibles Family
# class TheIncredibles(Family):
#     def __init__(self, last_name, members):
#         super().__init__(last_name, members)

#     def use_power(self, name):
#         for member in self.members:
#             if member['name'] == name and member['age'] >= 18:
#                 print(f"{name}'s power: {member['power']}")
#                 return
#         raise Exception(f"{name} is not over 18 years old.")

#     def incredible_presentation(self):
#         print("*Here is our powerful family**")
#         super().family_presentation()

# # Initial members for TheIncredibles
# incredibles_members = [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
# ]

# # Create an instance of TheIncredibles class
# incredibles_instance = TheIncredibles(last_name='Incredibles', members=incredibles_members)

# # Call the incredible_presentation method
# incredibles_instance.incredible_presentation()

# # Use the born method to add Baby Jack with the following power
# incredibles_instance.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='JackUnknown')

# # Call the incredible_presentation method again
# incredibles_instance.incredible_presentation()
