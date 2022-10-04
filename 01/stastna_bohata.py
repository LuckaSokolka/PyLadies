print('Odpovídej ano/ne')
print()

# program získá odpovědi
stastna = input('Jsi šťastná? ')
bohata = input('Jsi bohatá? ')
print()

# ošetření, že vstup může být napsán jakkoliv
stastna = stastna.lower()
bohata = bohata.lower()

# ošetření, že vstup je ano/ne
if (bohata != 'ano' and bohata != 'ne') and (stastna != 'ano' and stastna != 'ne'):
    print('Odpovídej pouze ano/ne. ')

#větev pro odpověď, že je šťastná
if stastna == 'ano':
    # je šťastná a zároveň bohatá
    if bohata == 'ano':
        print('Gratuluji!')
    # je šťastná, ale není bohatá
    elif bohata == 'ne':
        print('Zkus míň utrácet.')
# větev pro odpověď, že není šťastná
elif stastna == 'ne':
    # není šťastná a je bohatá
    if bohata == 'ano':
        print('Zkus se víc usmívat.')
    # není šťastná a není bohatá
    elif bohata == 'ne':
        print('To je mi líto.')

print()





