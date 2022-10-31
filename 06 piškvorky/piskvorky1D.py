def vyhodnot(pole):
    if 'xxx' in pole:
        print('Vyhrál X')
        exit()
    elif 'ooo' in pole:
        print('Vyhrál O')
        exit()
    elif '-' in pole == False: 
        print('Remíza')
        exit()
    else:
        print("Pokračujeme, nikdo nevyhrál.")
        
def tah_hrace(pole, pozice):
    while True:
        if pozice > 0 and pozice <= len(pole):
            if (pole[(int(pozice))-1] != 'x' and pole[(int(pozice))-1] != 'o'):
                pole[pozice - 1] = 'x'
                pole = ''.join(pole)
                return pole
            pozice = int(input("Políčko je obsazené, vyber jiné... "))
        pozice = int(input("Fungují jen celá, kladná čísla v rozmezí 1-20. Políčko: "))
    
    
     
from random import randrange

def tah_pocitace(pole):
    while True:
        pozice = randrange(1, 20)
        if pole[(int(pozice))-1] != 'x' and pole[(int(pozice))-1] != 'o':
            #pozice = int(pozice)
            pole[pozice - 1] = 'o'
            pole = ''.join(pole)
            return pole

herni_pole = "--------------------"
def piskvorky1d(herni_pole):
    while True:
        policko = int(input('Kam umístit X? Vyber políčko 1 - 20. Tvá volba: '))
        herni_pole = tah_hrace(list(herni_pole), policko)
        print("hráč:", herni_pole)
        #vyhodnot(herni_pole)
        herni_pole = tah_pocitace(list(herni_pole))
        print("PC", herni_pole)
        print(vyhodnot(herni_pole))

print(piskvorky1d(herni_pole))





