# Input ID number in Czech Republic
# write ouf corect/incorect ID

while True:
    # MONTHS 30 DAYS
    months_30_women = []
    months_30 = [4, 6, 9, 11]
    for month_30 in months_30:
        months_30_women.append(month_30 + 50)
    months_30 = months_30 + months_30_women

    # MONTHS 31 DAYS
    months_31_women = []
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    for mesic_31 in months_31:
        months_31_women.append(mesic_31 + 50)
    months_31 = months_31 + months_31_women

    years = list(range(86, 100)) + list(range(00, 23))
    only_numbers = []

    ID = list(input('Napiš rodné číslo: '))
    for number in ID:
        if number.isdigit():
            only_numbers.append(number)
            if len(only_numbers) == 10:
                modulo_eleven = int(''.join(only_numbers))
                year_ID = int(''.join(only_numbers[:2]))
                month_ID = int(''.join(only_numbers[2:4]))
                day_ID = int(''.join(only_numbers[4:6]))
                if (modulo_eleven % 11 == 0) and year_ID in years:

                    if (month_ID == 52 or month_ID == 2) and day_ID <= 29:
                        print('Zadané rodné číslo je v pořádku')
                        quit()
                    elif (month_ID in months_30) and day_ID <= 30:
                        print('Zadané rodné číslo je v pořádku')
                        quit()
                    elif (month_ID in months_31) and day_ID <= 31:
                        print('Zadané rodné číslo je v pořádku')
                        quit()
                    else:
                        print('Rodné číslo má formát xxxxxx/xxxx. Např. 123456/7809')
                        break
    print('Rodné číslo má formát xxxxxx/xxxx. Např. 123456/7809')
