import turtle
import random

pen = turtle. Turtle()
pen.speed(10)

def fancy_star(x,y,size,color): 
  pen.up()
  pen.pencolor(color)
  pen.goto(x,y)
  pen.down()
  for i in range(8):
    pen.forward(size)
    pen.right(135)

def average_star(x,y,size,color): 
  pen.up()
  pen.pencolor(color)
  pen.goto(x,y)
  pen.down()
  for o in range(5):
    pen.forward(size)
    pen.right(144)

def extrafancy_star(x,y,size,color):  
  pen.up()
  pen.pencolor(color)
  pen.goto(x,y)
  pen.down()
  for p in range(12):
    pen.forward(size)
    pen.right(150)

r3 = random.randint(10,200)
r6 = random.randint(10,200)
r9 = random.randint(10,200)

r1 = random.randint(-200,200)
r2 = random.randint(-200,200)
r4 = random.randint(-200,200)
r5 = random.randint(-200,200)
r7 = random.randint(-200,200)
r8 = random.randint(-200,200)

colours = ["red" , "orange" , "green" , "blue" , "indigo" , "purple" , "violet"]
random_color1 = random.choice(colours)
random_color2 = random.choice(colours)
random_color3 = random.choice(colours)

star = [fancy_star(r1,r2,r3,random_color1) , average_star(r4,r5,r6,random_color2) , extrafancy_star(r7,r8,r9,random_color3)]
  