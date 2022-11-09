from hangman_img import hangman_picture


def score(string, letter, attempt, word):
    """return result according to letter in/not in word"""

    if letter in word:
        return string

    elif letter not in word and attempt == 10:
        print("Visíš")
        return hangman_picture(attempt)

    elif letter not in word:
        return hangman_picture(attempt)
