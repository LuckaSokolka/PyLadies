# záměna písmene ve slově
retezec = input('Napiš slovo: ')
pozice = int(input('Na které pozici si přeješ změnu? '))
znak = input('A co tam napíšeme? :) ')

# složené nové slovo z části původního slova a vložené písmeno mezi části
print(retezec[:pozice - 1] + znak + retezec[pozice:])