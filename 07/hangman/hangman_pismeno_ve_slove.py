def installed_letter(word, letter, string):
    string = list(string)
    if letter in word:
        index_pismeno = word.index(letter)
        string[index_pismeno] = letter
        string = ''.join(string)
        return string
    else:
        string = ''.join(string)
        return string
