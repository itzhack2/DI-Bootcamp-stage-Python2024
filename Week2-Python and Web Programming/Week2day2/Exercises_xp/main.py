# 🌟 Exercise 1 : Set

# Create a set called my_fav_numbers with all your favorites numbers.
# my_fav_numbers = [ 7,10,1,11,]
# num_set=set(my_fav_numbers)
# print(num_set)
# Add two new numbers to the set.
# num_set.add(15)
# num_set.add(5)
# print(num_set)
# Remove the last number.
# num_set.remove(15)
# print(num_set)
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# friend_fav_numbers = [8,6,4,3]
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# our_fav_numbers = num_set.union(friend_fav_numbers) #1
# print(our_fav_numbers)
#print(friend_fav_numbers + my_fav_numbers) #2




# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?



# 🌟 Exercise 3: List
# Instructions
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket.remove('Banana')
# print(basket)
# basket.remove('Blueberries')
# print(basket)
# basket.append('Kiwi')
# print(basket)
# basket.insert(0,'Apples')
# print(basket)
# x = basket.count('Apples')
# print(x)
# basket.clear()
# print(basket)



# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

# list_num = [x/2 for x in range(3, 11)]
# print(list_num)




# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.


# for number in range(1,21):
#     print(number)

# print("All numbers from 1 to 20:")
# for num in range(1, 21):
#     print(num, end=' ')
# # print("\n")

# for num in range(1,21):
#     if num % 2 == 0:
#             print(num, end= ' ') 

# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
#
#  your_name = "itazhack"
# while True:
#     user_name = input("Please enter your name: ")
#     if user_name == your_name:
#         print("Welcome, {}! Exiting the loop.".format(your_name))
#         break
#     else:
#         print("Incorrect name. Please try again.")



# 🌟 Exercise 7: Favorite Fruits
        
# Instructions  
            
# Ask the user to input their favorite fruit(s) (one or several fruits).
        
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".

# Store the favorite fruit(s) in a list (convert the string of words into a list of words).

# Now that we have a list of fruits, ask the user to input a name of any fruit.

# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.

# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# fruit = [ 'mango','banana','apple','orange']
# print("Enter your favorite fruit:")
# fruit = input()
# print("i love," + fruit)
# for fruits in fruit:
# print(fruits)
# print('hello world'*8)





# 🌟 Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# toppings = []
# total_price = 10  # Base price for the pizza

# # Loop to get pizza toppings
# while True:
#     topping = input("Enter a pizza topping (or 'quit' to finish): ")

#     # Check if the user wants to quit
#     if topping.lower() == 'quit':
#         break

#     # Add the topping to the list
#     toppings.append(topping)

#     # Print a message saying the topping will be added
#     print(f"Adding {topping} to your pizza.")

# # Calculate the total price
# total_price += len(toppings) * 2.5

# # Print the toppings and total price
# print("\nYour pizza toppings:")
# for topping in toppings:
#     print("* " + topping)

# print(f"\nTotal price for your pizza: ${total_price:.2f}")



# 🌟 Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

def calculate_ticket_price(age):
    if age < 3:
        return 0 
    













# 🌟 Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich