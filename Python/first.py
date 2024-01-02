import turtle

turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(100)
squary.pencolor("skyblue")

for i in range(1000):
    squary.forward(i)
    squary.left(91)