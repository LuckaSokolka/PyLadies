# ZÁMĚNA PÍSMENE VE SLOVĚ

# slovo od uživatele
retezec = input('Napiš slovo: ')

# zadání pozice od uživatele a ošetření, že délka není kratší než pozice
pozice = int(input('Na které pozici si přeješ změnu? '))
while pozice > (len(retezec)) or (pozice <= 0):
    pozice = int(input('Pozice má být v rozmezí počtu písmen ve slově.\nZkus to ještě jednou. Pozice: '))

# znak na výměnu
znak = input('A co tam napíšeme? :) ')

# složené nové slovo z části původního slova a vložené písmeno mezi části
print(retezec[:(pozice - 1)] + znak + retezec[pozice:])


