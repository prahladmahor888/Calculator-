from turtle import*

speed(0)
bgcolor("black")
pensize(3)

for i in range(120):
    color("cyan")
    fd(i*2)
    lt(300)
    fd(i*2)
    rt(100)
    for i in range(2):
        rt(60)
done()