#pirveli davleba

list1=[1,2,456786543,"apple",False,232,2.4,True]

#pirvels vprintavt
print(list1[0])

#bolos vprintavt minus indexingit
print(list1[-1])

#pirvel sam elenmentis slicingi
print(list1[0:3])

#bolo xuti elementis slicingi
print(list1[2:7+1])

#stringsukuwyma vwert slcingit
string1 = "GOA IS THE BEST"
print(string1[::-1])

#vwert yovel mesame elements siidan
print(list1[::3])

#gavyot sia naxevrad
list2 = list1[0:4+1]
list3 = list1[5:8+1]

print(list2 , list3)


#meore davaleba

from turtle import *

#pirveli gza

penup()
goto(100,100)
pendown()

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

penup()
goto(-300,100)
pendown()

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

penup()
goto(-300,-300)
pendown()

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

penup()
goto(100,-300)
pendown()

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

#meore gza

penup()
goto(100,100)
pendown()

for i in range(4):
    forward(200)
    right(90)

penup()
goto(-300,100)
pendown()

for i in range(4):
    forward(200)
    right(90)

penup()
goto(-300,-300)
pendown()

for i in range(4):
    forward(200)
    right(90)

penup()
goto(100,-300)
pendown()

for i in range(4):
    forward(200)
    right(90)

#mesame gza

def draw_a_square(x_cordinate,y_cordinate):
    penup()
    goto(x_cordinate,y_cordinate)
    pendown()

    for i in range(4):
        forward(200)
        right(90)

draw_a_square(100,100)
draw_a_square(-300,100)
draw_a_square(-300,-300)
draw_a_square(100,-300)


exitonclick()
