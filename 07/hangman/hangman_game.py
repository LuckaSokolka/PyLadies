from hangman_settings import vytvor_retezec
from hangman_pismeno import pismeno
from hangman_score import score
from hangman_pismeno_ve_slove import dosazeni_pismene
from random import choice


def hangman_game(seznam):
    pokus = 0
    print()
    print('Hra: OBĚŠENEC')
    print('Uhádni písmeno ve slově a poskládej tak slovo')
    slovo = choice(seznam)
    retezec = vytvor_retezec(slovo)
    print(retezec)
    print(slovo)

    while True:
        pismenko_k_dosazeni = pismeno()
        retezec = dosazeni_pismene(slovo, pismenko_k_dosazeni, retezec)
        print()
        if pismenko_k_dosazeni not in slovo:
            pokus += 1
        print(score(retezec, pismenko_k_dosazeni, pokus, slovo))
        if "_" not in retezec:
            break
        elif pokus == 10:
            quit()


seznam = ("python", "kobra", "pyladies")

print(hangman_game(seznam))