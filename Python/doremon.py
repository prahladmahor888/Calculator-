from turtle import*
import colorsys
Screen().bgcolor("black")
speed(0)
h = 0.3
pensize(2)
def design(ang):
    circle(60+i,90)
    left(ang)
    circle(60+i,90)
    
for i in range(140):
    c = colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    design(90)
    design(120)
    h += 1/150
done()