''' Turtle graphics
PODZIMNÍ JEHLIČNANY :)  '''

from turtle import left, onclick, right, forward, shape, exitonclick, goto, up, down, color, speed,Screen
from turtle import penup, pendown,pencolor, colormode, pensize,bgcolor
from random import choice

colormode(255)
pensize(3)
bgcolor(246,244,210)

# proměnné používané pro vykreslení stromu
delka_vetve = 90
vzdalenost_vetvi = 20

# seznam podzimních barev
barvy = [(90,60,20),(156,39,6),(212,91,18),(243,188,46),(95,84,38)]

# počáteční souřadnice pro goto()
x = 800
y = 300

# řady 
for z in range (4):
    if z % 2 != 0:
        speed(10)
        up()
        # souřadnice nové řady
        goto((-x) + 75,(-y) + (z * 150))
        down()
    else:
        speed(10)
        up()
        goto((-x),(-y) + (z * 150))
        down()
# opakování pro k stromů 
    for k in range(7):
        penup()
        forward(delka_vetve * 2 + 10)
        left(90)
        pendown()
        color((choice(barvy)))

        #jednotlivý strom
        # zkracování délky větve až po vrchol
        for i in range( int(delka_vetve/10) + 1):
            # kmen
            forward(vzdalenost_vetvi)
            left(90)

            # větev na každou stranu
            for _ in range(2):
                penup()
                forward(delka_vetve - (i * 10))
                left(180)
                pendown()
                forward(delka_vetve - (i * 10))
            right(90)
        penup()
        right(180)
        # zpět tužka z vrcholu ke kmenu, počet pater * počet zkracování + kmen
        forward(i * vzdalenost_vetvi + vzdalenost_vetvi)
        left(90)
        pendown()
exitonclick()   