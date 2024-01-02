from turtle import*
import colorsys
bgcolor("black")
h = 0.5
pensize(2)
speed(100)
for i in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.01
    circle(30)
    backward(10)
    forward(9)
    circle(50)
    backward(1)
    right(50)
    forward(100)
    right(97)
    format(50)
    color(c)
done()