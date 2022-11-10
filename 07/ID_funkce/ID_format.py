def ID_format(ID):

    first_six_numbers = ID[:6]
    slash = ID[6]
    last_four_numbers = ID[7:]

    if first_six_numbers.isdigit() and last_four_numbers.isdigit() and slash == "/":
        return True
    else:
        print('Formát rodného čísla je 123456/7891. Obsahuje pouze čísla a lomítko.')
        return False
