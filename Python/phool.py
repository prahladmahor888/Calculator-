import turtle as t
t.pensize(5)
t.speed(40)
size = 250
n = 16
def draw():
    for c in ('green', 'blue', 'blue', 'green'):
        t.color(c)
        t.circle(-size/4,90)
        t.circle(size/4,90)
        t.left(90)
for i in range(n):
    draw()
    t.left(360/n)
t.done()
