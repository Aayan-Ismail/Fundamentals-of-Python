import turtle
pen = turtle. Turtle()
paper = turtle. Screen()
pen.speed(10)
pen.pensize(3)

def circlenew(x,y,z,c):
    pen.up()
    pen.color(c)
    pen.goto(x,y)
    pen.down()
    for i in range(36):
        pen.forward(z)
        pen.right(10)

circlenew(0,0,8,"blue")
circlenew(50,-50,8,"yellow")
circlenew(100,0,8,"black")
circlenew(150,-50,8,"green")
circlenew(200,0,8,"red")

turtle.done()


