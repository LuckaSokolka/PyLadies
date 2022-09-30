print('Odpovídej ano/ne')
# program získá odpovědi
stastna = str (input('Jsi šťastná? '))
bohata = str (input('Jsi bohatá? '))

#větev pro odpověď, že je šťastná
if stastna == 'ano':
    # je šťastná a zároveň bohatá
    if bohata == 'ano':
        print('Gratuluji!')
    # je šťastná, ale není bohatá
    elif bohata == 'ne':
        print('Zkus míň utrácet.')
# větev pro odpověď, že není šťastná
elif stastna =='ne':
    # není šťastná a je bohatá
    if bohata == 'ano':
        print('Zkus se víc usmívat.')
    # není šťastná a není bohatá
    elif bohata == 'ne':
        print('To je mi líto.')

# upozornění, když není odpověď ano/ne
if bohata !='ano' and bohata !='ne':
    print('Odpovídej pouze ano/ne')
elif stastna !='ano' and stastna !='ne':
    print('Odpovídej pouze ano/ne')





