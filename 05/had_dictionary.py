pets_sorted_with_second = []

# list key/ item
pets = [
    ('had'[1:], 'had'),
    ('andulka'[1:], 'andulka'),
    ('pes'[1:], 'pes'),
    ('kočka'[1:], 'kočka'),
    ('králík'[1:], 'králík')
]

# sort list
# output: [('ad', 'had'), ('es', 'pes'), ('ndulka', 'andulka')....
pets.sort()
# transfer to dictionary
lined_up_dict = dict(pets)
# print only complete str in right order
for pet in lined_up_dict.values():
    pets_sorted_with_second.append(pet)
print(pets_sorted_with_second)
