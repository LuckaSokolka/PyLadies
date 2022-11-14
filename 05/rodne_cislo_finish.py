# Input ID number in Czech Republic
# write ouf corect/incorect ID


# MONTHS 30 DAYS
months_30 = [4, 6, 9, 11]

# MONTHS 31 DAYS
months_31 = [1, 3, 5, 7, 8, 10, 12]

# YEARS
years = list(range(86, 100)) + list(range(00, 23))

while True:

    ID = input('Napiš rodné číslo: ')
    if len(ID) != 11:
        print("Nesprávná délka rodného čísla.")
        continue

    only_numbers = (ID.replace('/', ''))
    if not only_numbers.isdigit() and ID[6] != "/":
        print("Nesprávný formát.")
        continue

    modulo_eleven = int(only_numbers)
    year_ID = int(only_numbers[:2])
    month_ID = int(only_numbers[2:4])
    day_ID = int(only_numbers[4:6])
    end = int(only_numbers[6:])

    if end > 6000:
        print('Rodné číslo je nevalidní')
        continue

    if modulo_eleven % 11 == 0 and (year_ID in years):

        if month_ID % 50 == 2 and day_ID <= 29:
            print('Zadané rodné číslo je v pořádku')
            break
        elif month_ID % 50 in months_30 and day_ID <= 30:
            print('Zadané rodné číslo je v pořádku')
            break
        elif month_ID % 50 in months_31 and day_ID <= 31:
            print('Zadané rodné číslo je v pořádku')
            break
        else:
            print('Rodné číslo je nevalidní.')
    else:
        print('Rodné číslo je neplatné. Zkontrolujte, že je správně zadané.')
