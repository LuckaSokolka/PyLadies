def dosazeni_pismene(slovo, pismeno, retezec):
    retezec = list(retezec)
    if pismeno in slovo:
        index_pismeno = slovo.index(pismeno)
        retezec[index_pismeno] = pismeno
        retezec = ''.join(retezec)
        return retezec
    else:
        retezec = ''.join(retezec)
        return retezec
