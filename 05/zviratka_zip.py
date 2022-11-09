pets = ['had', 'andulka', 'pes', 'kočka', 'králík']
pets_start_second = []
pets_sorted = []

for pet in pets:
    pets_start_second.append(pet[1:])
pets_and_pets_second = list(zip(pets_start_second, pets))
pets_and_pets_second.sort()
for animal in pets_and_pets_second:
    pets_sorted.append(animal[1])
print(pets_sorted)
