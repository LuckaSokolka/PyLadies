# HRA KÁMEN/NŮŽKY/PAPÍR

print("Zahrajeme si Kámen - Nůžky - Papír!")
print()

# přiřazení kámen/nůžky/papír do proměnné pc a její převedení na str
from random import randrange                           
pc = randrange(3)
pc = str(pc)  

# žádáme vstup od hráče
hrac = input("Vyber si (kámen/nůžky/papír): ")
print()

# převede vstup celý na malý
hrac = str(hrac.lower())

# přiřazení do proměnné člověk 
if (hrac == 'kámen') or (hrac == 'kamen'):
    hrac = '2'
elif (hrac == 'nuzky') or (hrac == 'nůžky'):
    hrac = '1'
elif (hrac == 'papír') or (hrac == 'papir'):
    hrac = '0'
else:
    print("Zadej jen kámen/nůžky/papír. Jinak nemůžeme hrát...")
    quit()

# if-elif, pro vypsání výsledku, dle klasické hry kámen/nůžky/papír
if pc == hrac:
    print("Plichta.")
elif (pc == "2" and hrac == "1") or (pc == "1" and hrac == "0") or (pc == "1" and hrac== "3"):
    print("Počítač vyhrál.")
elif (hrac == "2" and pc == "1") or (hrac == "1" and pc == "0") or (hrac == "1" and pc=="3"):
    print("Vyhrál jsi!")
else:
    print("Taková možnost není.")

print()
