# HRA KÁMEN/NŮŽKY/PAPÍR
print()
print("Zahrajeme si Kámen - Nůžky - Papír!")
print()

# přiřazení kámen/nůžky/papír do proměnné pc a její převedení na str
from random import randrange                           
pc = randrange(3)
pc = str(pc)

# žádáme vstup od hráče
hrac = input('Vyber si: \n kámen = 2 \n nůžky = 1 \n papír = 0 \n tvá volba: ')
print()
if hrac > '3':
    print('Vybírej jen čísla od 0, 1, 2. ')
    quit()

print('hráč:', hrac)
print('pc:', pc)
print()

if pc > hrac:
    if pc == '2' and hrac == '0':
        print('Vyhrál jsi!')
    else:
        print('Počítač vyhrál.')
elif hrac > pc:
        if hrac == '2' and pc == '0':
            print('Počítač vyhrál')
        else:
            print('Vyhrál jsi!')
elif pc == hrac:
    print('Plichta')

print()
