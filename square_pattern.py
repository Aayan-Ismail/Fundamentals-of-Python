import turtle
pen = turtle. Turtle()
pen.speed(0)

def square_rotating(x,y,c):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.pencolor(c)
    for i in range(36):
        pen.right(10)

        for i in range(4):
            pen.forward(60)
            pen.right(90)


square_rotating(-450,450,"red")
square_rotating(450,450,"yellow")
square_rotating(-450,-450,"green")
square_rotating(450,-450,"blue")

turtle.done()

