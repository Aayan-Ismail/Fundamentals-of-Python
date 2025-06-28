import turtle
pen = turtle. Turtle()
paper = turtle. Screen()
pen.pencolor('black')
pen.speed(9)

x = int(input("enter the pen size you would like: "))
pen.pensize(x)

clr = input("color: ")
pen.fillcolor(clr)

pen.begin_fill()
#head
pen. circle(30)
pen.end_fill()

pen.fillcolor(clr)
pen.begin_fill()
#for loop - body
for i in range(36):
  pen.forward(10)
  pen.right(10)
pen.end_fill()
  
paper. bgcolor('white')

#left eye
pen.up()
pen.goto(-10,35)
pen.down()
pen.circle(5)

#right eye
pen.up()
pen.goto(10,35)
pen.down()
pen.circle(5)

#smile
pen.up()
pen.goto(-10,25)
pen.down()
pen.right(90)

for i in range(18):
  pen.forward(1.5)
  pen.left(10)

#button
pen.up()
pen.goto(0,-30)
pen.dot('black')
pen.goto(0,-45)
pen.dot('black')
pen.goto(0,-60)
pen.dot('black')

pen.pensize(2)
#right arm
pen.up()
pen.goto(0,0)
pen.down()
pen.goto(80,0)
pen.goto(80,50)

#left arm
pen.up()
pen.goto(0,0)
pen.down()
pen.goto(-80,0)
pen.goto(-80,-50)
pen.up()

pen.fillcolor('red')

pen.pensize(1)
pen.goto(-25,60)
pen.begin_fill()
pen.down()
pen.right(90)
pen.forward(50)
pen.left(135)
pen.goto(0,100)
pen.goto(-25,60)
pen.end_fill()
turtle.done()