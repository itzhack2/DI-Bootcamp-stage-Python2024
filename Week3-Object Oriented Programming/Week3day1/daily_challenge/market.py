# Instructions : Old MacDonald’s Farm
class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        info = f"{self.farm_name}'s farm\n"
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
        info += "E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        animal_types = self.get_animal_types()
        num_animals = len(animal_types)
        if num_animals == 0:
            return f"{self.farm_name}'s farm has no animals."
        elif num_animals == 1:
            animal_str = animal_types[0]
        else:
            animal_str = ', '.join(animal_types[:-1]) + f" and {animal_types[-1]}"
        return f"{self.farm_name}'s farm has {animal_str}{'s' if num_animals > 1 else ''}."
    
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print("\nAnimal types in the farm:", macdonald.get_animal_types())
print("\nShort farm info:", macdonald.get_short_info())
