pets = ['had', 'andulka', 'pes', 'kočka', 'králík']
pets_start_second = []

for pet in pets:
    pets_start_second.append(pet[1:]) 
pets_sorted_second = zip(pets_start_second, pets)
pets_sorted_second = list(pets_sorted_second)
pets_sorted_second.sort()
for animal in pets_sorted_second:
    print(animal[1], end=" ")
    