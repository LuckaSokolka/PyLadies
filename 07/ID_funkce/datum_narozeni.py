def birthdate(ID):

    year = int(ID[:2])
    if year > 85 and year < 100:
        year = 1900 + int(year)
    elif year < 24:
        year = 2000 + int(year)

    month = int(ID[2:4]) % 50
    day = ID[4:6]
    return (f" {day}.{month}.{year}")
