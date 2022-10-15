diacritics = ['á', 'é', 'í', 'ó', 'ú', 'ý', 'č', 'ď', 'ě', 'ň', 'ř', 'š', 'ť', 'ž', 'ů']
ASCII_numbers = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58]

key = input('key ')
for znak in key:
    znak_ASCII = ord(znak)
    if znak_ASCII not in ASCII_numbers:
        key = int(input('Zadávej jen celá, kladná čísla. Příklad: 2, 5, 15 \nKey: '))

key = int(key)

if key <= 0:
    key = int(input('Key můžou být jen celá, kladná čísla. Příklad: 2, 5, 15 \nKey: '))

plain_text = input('plain text ')
for character in plain_text:
    if character in diacritics:
        plain_text = input('Bez čísel a diakritiky. Příklad: les, pes, jedna \nPlain text: ')
    elif character.isnumeric():
        plain_text = input('Bez čísel a diakritiky. Příklad: les, pes, jedna \nPlain text: ')
plain_text = plain_text.lower()

'''
ord(character) -> transfer character to number in ASCII
... + key -> shift of key
... - 97 -> in ASCII start alphabet with number 97,
    (- 97) made the same order like in alphabet
... % 26 -> secure that 'Z' will by continue from the beginning of the alphabet,
    alphabet have 26 characters
... + 97 -> assign number in ASCII
... chr -> transfer number to character

'''

for character in plain_text:
    if character.isalpha():
        ciper = chr(((ord(character)) + int(key) - 97) % 26 + 97)
        print(ciper, end="")
    else:
        print(character, end="")
print()
