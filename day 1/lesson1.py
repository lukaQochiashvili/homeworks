from turtle import color, exitonclick, forward, goto, left, pendown, right, speed, width
#starting creating a house

#started making a square
speed(30)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#ended making square

#started creating roof for a house
forward(70)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)


forward(80)
left(90)
forward(200)
color("blue")
left(40)
forward(150)
left(98)
forward(150)

#ended creating roof

#started making windows

#started making 1st window

color("red")
goto(0, 0)
pendown()
right(228)
forward(70)
left(90)
forward(70)
left(90)
color("brown")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
width(3)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)
left(90)
forward(25)
right(90)
color("red")
forward(20)
left(90)
#ended making first window

width(7)
forward(50)
left(90)
forward(25)
right(90)
color("brown")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
color("red")
forward(50)
left(90)
color("brown")
forward(25)
width(3)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)

#ended making windows

left(90)
color("red")
width(7)
forward(50)
right(90)
forward(50)
right(90)
forward(100)

exitonclick()

