def field(columns, lines):

    memofield = []

    for i in range(columns):
        temp = []
        for j in range(lines):
            temp.append("█")
        memofield.append(temp)
    return memofield

def game_field():
    for seznam in field(4,4):
        print(" ")
        for prvek in seznam:
            print(prvek, end=" ")
        print(end="\n")

vykresleni_pole()
