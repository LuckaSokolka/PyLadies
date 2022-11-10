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
