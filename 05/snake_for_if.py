pets_start_second = []
pets_sorted = []
pets = ['had', 'andulka', 'pes', 'kočka', 'králík']
copy_pets = pets

for pet in pets:
    pet = pet[0] + pet[1:]
    pets_start_second.append(pet[1:])
    pets_start_second.sort()
for pet_second in pets_start_second:
    for animal in copy_pets:
        animal = animal[0] + animal[1:]
        if pet_second == animal[1:]:
            pets_sorted.append(animal)

print(pets_sorted)
