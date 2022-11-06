from hangman_img import obesenec


def score(retezec, pismeno, pokus, slovo):

    if pismeno in slovo:
        return retezec

    elif pismeno not in slovo and pokus == 10:
        print("Visíš")
        return obesenec(pokus)

    elif pismeno not in slovo:
        return obesenec(pokus)

    elif "_" not in retezec:
        return "Unikl jsi katovi."
