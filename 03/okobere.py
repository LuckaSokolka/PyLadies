# OKO BERE 
''' hráč si nechává otáčet karty, pokud je jejich součet = 21  vyhrál,
 pokud je součet > 21 prohrál '''
from random import randrange
soucet = 0
odpoved = 'ano'

# dokud chce hráč přidávat karty, tak funguje smyčka
while odpoved == 'ano':
    karta = randrange(2,11)
    soucet += karta

    if soucet < 21:
        print(f'Otočil jsi: {karta} a součet je {soucet}')
        odpoved = input(f'Chceš pokračovat? ')
        odpoved = odpoved.lower()
        if odpoved != ('ano') and odpoved != ('ne'):
            odpoved = input('Prosím, odpovídej pouze ano nebo ne. Pokračujeme? ')
    elif soucet == 21: 
        print(f'Vyhrál jsi! Vytáhl sis: {karta}. Tvůj součet je {soucet}')
        break
    elif soucet > 21:
        print(f'Prohrál jsi. Lízl sis: {karta}. Součet {soucet} > 21.')
        break
if odpoved == 'ne':
    print(f'Škoda. Měl jsi {soucet}. Do 21ti ti chybělo {21 - soucet}')



