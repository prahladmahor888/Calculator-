import turtle as t

t.bgcolor("black")
t.pensize(2)
t.speed(10)

def Draw_circle():
    t.setposition(0,-200)
    t.pendown()
    t.pensize(5)
    t.pencolor("white")
    t.begin_fill()
    t.fillcolor("red")
    t.circle(200)
    t.end_fill()
    t.penup()
    
def draw_circle2():
    t.setposition(0,-150)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(150)
    t.end_fill()
    t.penup()
    
def draw_A():
    t.setposition()
    
Draw_circle()
draw_circle2()
t.done()