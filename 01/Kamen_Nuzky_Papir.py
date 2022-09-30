                                                        # HRA KÁMEN/NŮŽKY/PAPÍR
print("Zahrajeme si Kámen - Nůžky - Papír!")
print()
hrac = str(input("Vyber si (kámen/nůžky/papír): "))
print()

from random import randrange                            # náhoda
cislo = randrange(3)                                    # vybere čislo od 0-2 a přiřadí kamen, nuzky, papir do proměnné pc
if cislo == 0:
    pc = "kámen"
elif cislo == 1:
    pc = "nůžky"
else: 
    pc = "papír"

print("tvá volba: ", hrac)
print("protihráč: ", pc)
print()

                                                      # ošetření, možnosti, napsat slovo jakkoliv
if pc == "kámen" or pc== "KÁMEN" or pc== "Kámen" or pc=="KAMEN" or pc== "KÁMEN":
    pc = "kamen"
if hrac == "kámen" or hrac == "KÁMEN" or hrac == "Kámen" or hrac == "KAMEN" or hrac == "kamen":
    hrac = "kamen"
if pc == "Papír" or pc == "Papir" or pc == "papír" or pc == "PAPIR" or pc== "PAPÍR" or pc == "papir":
    pc = "papir"
if hrac == "Papír" or hrac == "Papir" or hrac == "papír" or hrac == "PAPIR" or hrac == "PAPÍR" or hrac == "papir":
    hrac = "papir"
if pc == "nůžky" or pc == "nuzky" or pc == "Nuzky" or pc == "Nůžky" or pc == "NŮŽKY" or pc == "NUZKY":
    pc = "nuzky"
if hrac == "nůžky" or hrac == "nuzky" or hrac == "Nuzky" or hrac == "Nůžky" or hrac == "NŮŽKY" or hrac == "NUZKY":
    hrac = "nuzky"

                                                        # if-elif, pro vypsání výsledku, dle klasické hry kámen/nůžky/papír
if pc == hrac:
    print("Plichta.")
elif (pc == "kamen" and hrac == "nuzky") or (pc == "nuzky" and hrac == "papir") or (pc == "papir" and hrac=="kamen"):
    print("Počítač vyhrál.")
elif (hrac == "kamen" and pc == "nuzky") or (hrac == "nuzky" and pc == "papir") or (hrac == "papir" and pc=="kamen"):
    print("Vyhrál jsi!")
else:
    print("Taková možnost není.")

print()