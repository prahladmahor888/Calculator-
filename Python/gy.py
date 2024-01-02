import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(100)
def draw():
    h = 0
    n = 28
    t.up()
    t.goto(0,40)
    t.down()
    t.pensize(2)
    for i in range(80):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 1/n
        t.color(c)
        t.forward(30.63)
        t.circle(i,5)
        for j in range(i):
            t.forward(25)
            t.right(90)
            t.back(10)
            t.circle(j,3.5)
            t.right(90.01)
            
draw()
for k in range(47):
    draw()
t.done()