diacritics = ['á', 'é', 'í', 'ó', 'ú', 'ý', 'č', 'ď', 'ě', 'ň', 'ř', 'š', 'ť', 'ž', 'ů']

key = input('key: ')
while key.isdigit() is False:
    try:
        a = int(key)
    except ValueError:
        print('Jako key je možné použít pouze celé číslo.')
        key = input('key: ')

plain_text = input('plain text: ')

for character in plain_text:
    if character.isalnum():
        if character in diacritics:
            print(character, end="")
        elif character.isnumeric():
            ciper = chr(((ord(character)) + int(key) - 48) % 10 + 48)
            print(ciper, end="")
        elif character.isupper():
            ciper = chr((ord(character) + int(key) - 65) % 26 + 65)
            print(ciper, end="")
        elif character.islower:
            ciper = chr(((ord(character)) + int(key) - 97) % 26 + 97)
            print(ciper, end="")
    else:
        print(character, end="")
print()

'''
ord(character) -> transfer character to number in ASCII
... + key -> shift of key
... - 97 -> in ASCII start alphabet with number 97,
    (- 97) made the same order like in alphabet
... % 26 -> secure that 'Z' will by continue from the beginning of the alphabet,
    alphabet have 26 characters
... + 97 -> assign number in ASCII
... chr -> transfer number to character'''
