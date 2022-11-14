def ID_format(ID):

    first_six_numbers = ID[:6]
    slash = ID[6]
    last_four_numbers = ID[7:]

    if (first_six_numbers.isdigit() and len(first_six_numbers) == 6
            and last_four_numbers.isdigit() and len(last_four_numbers) == 4
            and slash == "/"):
        return True
    else:
        print("Rodné číslo může obsahovat pouze čísla a lomítko.")
        print("Formát rodného čísla: 000000/0000")
        return False
