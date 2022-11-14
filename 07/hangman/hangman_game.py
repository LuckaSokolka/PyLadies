from random import choice
from hangman_score import score
from hangman_letter_in_word import create_string, installed_letter


# HANGMAN GAME
# guess letter in word and find the whole word

def hangman_game(inventory):

    attempt = 0
    print()
    print('Hra: OBĚŠENEC')
    print('Uhádni písmeno ve slově a poskládej tak slovo')
    word = choice(inventory)  # random word
    string = create_string(word)  # keep the word secret
    print(string)

    while "_" in string and attempt < 10:

        letter_to_install = input("Hádej písmeno ")
        string = installed_letter(word, letter_to_install, string)
        print()
        if letter_to_install not in word:
            attempt += 1
        print(score(string, letter_to_install, attempt, word))

    if "_" not in string:
        print('Unikl jsi katovi! Dobrá práce :)')


inventory = ("python", "kobra", "pyladies")
print(hangman_game(inventory))
