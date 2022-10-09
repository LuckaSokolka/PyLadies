clovek = input("Kamen/nuzky/papir ")

clovek = clovek.lower()
print(clovek)

if (clovek == 'kámen') or (clovek == 'kamen'):
    clovek = '2'
elif (clovek == 'nuzky') or (clovek == 'nůžky'):
    clovek == '1'
elif (clovek == 'papír') or (clovek == 'papir'):
    clovek == '0'