from ID_format import ID_format
from modulo_eleven import modulo_eleven
from datum_narozeni import birthdate
from gender import gender


def control_ID():

    while True:
        ID = input("Zadej rodné číslo ")
        if ID_format(ID) is True and modulo_eleven(ID) is True:
            print("Rodné číslo je v pořádku.")
            print(f"Datum narození: {birthdate(ID)}")
            print(f"pohlaví: {gender(ID)}")
            break
        else:
            print("Rodné číslo je neplatné.")


control_ID()
