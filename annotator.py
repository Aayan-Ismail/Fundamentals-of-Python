import turtle
p1 = turtle. Turtle()
p2 = turtle. Turtle()
paper = turtle. Screen()

def go_forward():
    p1.forward(movement)

def go_up():
    p1.setheading(90)

def go_down():
    p1.setheading(270)

def goright():
    p1.setheading(0)

def goleft():
    p1.setheading(180)

def click(x,y):
    paper.tracer(0)
    p1.setheading(p1.towards(x,y))
    paper.tracer(1)

def drag(x,y):
    paper.tracer(0)
    p1.goto(x,y)
    paper.tracer(1)

paper.listen()
paper.onkey(go_up, "w")
paper.onkey(go_down, "s")
paper.onkey(goright, "d")
paper.onkey(goleft, "a")
paper.onkey(go_forward, "space")

userword = input("write what you want to see on the screen. ")
size = int(input("write the number which will be the size of the text. "))
movement = int(input("how many steps do you want the turtle to take? "))
p2.write(userword, font=("georgian", size , "bold"))

p2.color("green")
p1.color("red")
p1.shape("turtle")

paper.onscreenclick(click)
p1.ondrag(drag)

turtle.done()