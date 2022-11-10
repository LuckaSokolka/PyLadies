<<<<<<< HEAD
def creat_string(word):
    string = len(word) * "_"
    return string

def installed_letter(word, letter, string):
    """put letter in right place in string"""

    string = list(string)
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                string[i] = letter
        string = ''.join(string)
        return string
    else:
        string = ''.join(string)
        return string
=======
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
>>>>>>> 69623d0eb3daae941bfb622f978f77ba46a00aad
