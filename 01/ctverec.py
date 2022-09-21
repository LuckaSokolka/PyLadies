strana = float(input('Zadej číslo: '))  # v centimetrech
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod čtverce, se stranou délky',strana,'je:', strana * 4,'cm')
    print('Obsah čtverce, se stranou délky',strana,'je:', strana **2,'cm2')
else:
    print('Strana musí být kladná, jinak z toho nebude čtverec!')

print('Děkujeme za použití geometrické kalkulačky.')