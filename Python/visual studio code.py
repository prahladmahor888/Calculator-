import turtle
from math import sqrt
t = turtle.Turtle()
turtle.colormode(255)
s = turtle.Screen().bgcolor("black")
t.speed(-10)
#fold1
t.begin_fill()
t.color((19,184,255))
t.fillcolor((19,184,255))
t.penup()
t.goto(0,-100)
t.pendown()
t.left(90)
t.forward(200)
t.left(225)
t.forward(50)
t.right(45)
t.forward(130.5)
t.right(45)
t.forward(50)
t.end_fill()
#fold 2
t.begin_fill()
t.color((35,146,245))
t.fillcolor((35,146,245))
t.right(90)
t.forward(200)
t.circle(-5,170)
t.forward(166)
t.end_fill()
#fold 3
t.begin_fill()
t.color((13,123,244))
t.fillcolor((13,123,244))
t.penup()
t.goto(0,100)
t.pendown()
t.right(100)
t.forward(200)
t.circle(5,170)
t.forward(167)
t.end_fill()
t.hideturtle()

t.penup()
t.goto(-200,-170)
t.pendown()
t.write("Visual Studio", font=('Arial',38,'bold'))
t.penup()
t.goto(-100,-220)
t.pendown()
t.write("Code", font=('Arial',34,'bold'))
turtle.done()