from hangman_settings import creat_string
from hangman_score import score
from hangman_pismeno_ve_slove import installed_letter
from random import choice


def hangman_game(inventory):

    attempt = 0
    print()
    print('Hra: OBĚŠENEC')
    print('Uhádni písmeno ve slově a poskládej tak slovo')
    word = choice(inventory)
    string = creat_string(word)
    print(string)

    while "_" in string and attempt < 10:

        letter_to_installed = input("Hádej písmeno ")
        string = installed_letter(word, letter_to_installed, string)
        print()
        if letter_to_installed not in word:
            attempt += 1
        print(score(string, letter_to_installed, attempt, word))
    print('Unikl jsi katovi! Dobrá práce :)')


inventory = ("python", "kobra", "pyladies")
print(hangman_game(inventory))
