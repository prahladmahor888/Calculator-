from turtle import*
import colorsys
bgcolor("black")
pensize(3)
speed(100)
h = 0.001
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.01
    forward(50)
    left(180)
    forward(50)
    right(60)
    forward(50)
    left(60)
    forward(50)
    right(60)
    forward(50)
    left(90)
    forward(50)
    right(270)
    forward(50)
    right(0)
    forward(1)
done()