from turtle import *


#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing door
forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of door

#making roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#finished roof

#making windows
penup()
goto(10, 170)
pendown()
color("brown")
begin_fill()
left(120)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)
end_fill()

penup()
goto(190, 170)
pendown()
color("brown")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#finished making windowws

exitonclick()