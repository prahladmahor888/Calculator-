import turtle as t

t.bgcolor("black")
t.speed(99)
t.pensize(4)

def Draw_circle():
    t.setposition(0,-200)
    t.pendown()
    t.pensize(4)
    t.pencolor("white")
    t.begin_fill()
    t.fillcolor("red")
    t.circle(200)
    t.end_fill()
    t.penup()
    
def Draw_circle2():
    t.setposition(0,-170)
    t.pendown()
    t.pensize(4)
    t.pencolor("white")
    t.begin_fill()
    t.fillcolor("black")
    t.circle(170)
    t.end_fill()
    t.penup()

def Draw_circle3():
    t.setposition(0,-65)
    t.penup()
    t.pensize(4)
    t.pencolor("red")
    t.begin_fill()
    t.fillcolor("red")
    t.left(180)
    t.forward(120)
    t.left(90)
    t.forward(40)
    t.left(50)
    t.forward(50)
    t.left(40)
    t.forward(165)
    t.left(40)
    t.forward(50)
    t.left(50)
    t.forward(40)
    t.left(90)
    t.forward(120)
    t.pendown()
    t.end_fill()
    
def draw_write():
    t.setposition(0,-80)
    t.pencolor("green")
    t.write('TM',font=('Verdana',120,'bold'),align='center')

def draw_writeA():
    t.setposition(0,-97)
    t.penup()
    t.pencolor("white")
    t.pendown()
    t.write('Technical',font=('Verdana',18,'bold'),align='center')
     
def draw_writeb():
    t.setposition(0,-120)
    t.pencolor("white")
    t.write('Mahour',font=('Verdana',18,'bold'),align='center')

Draw_circle()
Draw_circle2()
Draw_circle3()
draw_write()
draw_writeA()
draw_writeb()
t.hideturtle()
t.done()