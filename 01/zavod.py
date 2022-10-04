# Závod se zvířátky 
# 
# dotazovaný zadá rychlost, jakou chce běžet (km/h)                                                                       
zavodnik = input('Zadej rychlost, kterou poběžíš [km/h]... ')

# konrola vstupu
try:
    a = float(zavodnik)
except ValueError:
    print('Rychlost nebyla zadaná ve správném formátu.Uveď ji prosím jako celé nebo desetinné číslo, např. 5.5, 15, 10.7')
    quit()
    
# převod str na float
zavodnik = float(zavodnik)
# dle rychlosti se vybere podmínka a přiřadí zvířátko
if zavodnik >= 120:                                                    
    print('WOW! Nehoří ti nohy? Ty jsi určitě Sonic!')
elif zavodnik < 120 and zavodnik >= 90:
    print('Člověče...můžeš závodit s gepardem')
elif zavodnik < 90 and zavodnik >= 60:
    print('Tak tady už máš konkurenci vysokou. Běžíš jako o život. Skoro jako gazela, antilopa nebo zajíc...')
elif zavodnik < 60 and zavodnik >= 30:
    print('Tady bacha, může tě dohonit pštros.')
elif zavodnik < 30 and zavodnik >= 10:
    print('Dobrý!Můžeš předběhnout čmeláka.')
elif zavodnik < 10 and zavodnik >= 1:
    print('Bacha na hlemýždě. Je ti v patách.')
else:
    print('Tak toto už je souboj jeden na jednoho. Ty a želva.')

