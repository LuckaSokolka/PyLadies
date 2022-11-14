def modulo_eleven(ID):
    ID_only_numbers = ID[:6] + ID[7:]
    modulo_eleven = int(ID_only_numbers)
    if modulo_eleven % 11 == 0:
        return True
