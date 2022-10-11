# OKO BERE 
''' hráč si nechává otáčet karty, pokud je jejich součet = 21  vyhrál,
 pokud je součet > 21 prohrál '''
from random import randrange
soucet = 0
odpoved = 'ano'

# Zahájení
print()
print('Vitej ve hře OKO BERE')
print()
print('Pravidla: Lížeš si kartu dokud tvůj součet není roven 21. Pokud je součet > 21, prohrál jsi.')

# dotaz na první kartu a ošetření, že kód neproběhne, pokud hráč nechce pokračovat
prvni_karta = input('Můžeme začít? ')
prvni_karta = prvni_karta.lower()

if prvni_karta == 'ne':
    print('Tak třeba příště.')
    quit()
elif prvni_karta != 'ne' and prvni_karta != 'ano':
    print('Nevím jak tomu rozumět. Odpovídej pouze ano/ne.')
    prvni_karta = input('Hrajem? ')
    prvni_karta = prvni_karta.lower()

    if prvni_karta == 'ne':
        print('Na shledanou. :)')
        quit()

# dokud chce hráč přidávat karty, tak funguje smyčka
while odpoved == 'ano':
    karta = randrange(2,11)
    soucet += karta

    if soucet < 21:
        print(f'Otočil jsi {karta} a součet je {soucet}')
        odpoved = input('Chceš pokračovat? ')
        odpoved = odpoved.lower()
        if odpoved != ('ano') and odpoved != ('ne'):
            odpoved = input('Prosím, odpovídej pouze ano nebo ne. Pokračujeme? ')
    elif soucet == 21: 
        print(f'Vyhrál jsi! Vytáhl sis {karta}. Tvůj součet je {soucet}')
        break
    elif soucet > 21:
        print(f'Prohrál jsi. Lízl sis {karta}. Součet {soucet} > 21.')
        break
if odpoved == 'ne':
    print(f'Měl jsi {soucet}. Do 21 chybělo {21 - soucet}')
print()
print('Děkujeme za hru.')
print()



