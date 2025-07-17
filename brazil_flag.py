import turtle
pen = turtle. Turtle()
paper = turtle. Screen()
pen.speed(0)

def star(x,y): 
    pen.up()
    pen.pencolor("white")
    pen.goto(x,y)
    pen.down()
    for i in range(5):
        pen.forward(15)
        pen.right(144)

def rectangle(x,y,f,d,c):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.fillcolor(c)
    pen.begin_fill()
    for i in range(2):
        pen.forward(f)
        pen.right(90)
        pen.forward(d)
        pen.right(90)
    pen.end_fill()
    pen.up()

rectangle(-400,0, 800, 500, "green")

#rhombus
pen.up()
pen.goto(0,-450)
pen.right(150)
pen.down()
pen.fillcolor("yellow")
pen.begin_fill()
for i in range(2):
   pen.right(60)
   pen.forward(400)
   pen.right(120)
   pen.forward(400)
pen.end_fill()
pen.up()

#circle
pen.goto(-75,-130)
pen.fillcolor("blue")
pen.begin_fill()
pen.circle(135)
pen.end_fill()

pen.right(30)
rectangle(127,-250,267,25,"white")
star(-20,-220)
star(50,-220)
star(-30,-210)
star(-20,-300)
star(15,-292)
star(30,-310)
star(-10,-320)
star(-30,-210)
star(10,-280)

turtle.done()