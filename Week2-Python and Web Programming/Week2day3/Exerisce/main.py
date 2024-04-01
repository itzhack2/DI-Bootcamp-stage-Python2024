#  Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
x = zip(keys,values)
print(tuple(x))


# Exercise 2: Cinemax
family = {}
while True:
    name = input("Enter family member's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

total_cost = 0
for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} has to pay ${cost}")
    total_cost += cost

print("Total cost for the family:", total_cost)


# Exercise 3: Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
# 3. Change the number of stores to 2.
brand["number_stores"] = 2
# 4. Print a sentence that explains who Zara's clients are.
print("Zara's clients are men, women, children, and home decorators.")
# 5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
# 7. Delete the information about the date of creation.
del brand["creation_date"]
# 8. Print the last international competitor.
print("Last international competitor:", brand["international_competitors"][-1])
# 9. Print the major clothes colors in the US.
print("Major clothes colors in the US:", brand["major_color"]["US"])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print("Number of key-value pairs:", len(brand))
# 11. Print the keys of the dictionary.
print("Keys of the dictionary:", list(brand.keys()))
# 12. Create another dictionary called more_on_zara with the following details:
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?
print("Number of stores after update:", brand["number_stores"])
# The value of key "number_stores" got updated to 10000.


# Exercise 4: Disney Characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Recreate the 1st result
disney_users_A = {user: i for i, user in enumerate(users)}
print(disney_users_A)
# Recreate the 2nd result
disney_users_B = {i: user for i, user in enumerate(users)}
print(disney_users_B)
# Recreate the 3rd result
disney_users_C = dict(sorted({user: i for i, user in enumerate(users)}.items()))
print(disney_users_C)
