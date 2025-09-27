import turtle
import random

p = turtle. Turtle()
p.speed(0)
p.up()
p.goto(500,50)
p.right(90)
p.down()
p.forward(150)
p.up()

speed1 = random.randint(0,10)
speed2 = random.randint(0,10)
speed3 = random.randint(0,10)
speed4 = random.randint(0,10)

p1 = turtle. Turtle()
p1.shape("turtle")
p1.color("red")
p1.speed(speed1)
p1.up()
p1.forward(500)

p2 = turtle. Turtle()
p2.shape("turtle")
p2.color("yellow")
p2.up()
p2.goto(0,50)
p2.speed(speed2)
p2.forward(500)

p3 = turtle. Turtle()
p3.shape("turtle")
p3.color("green")
p3.up()
p3.goto(0,-50)
p3.speed(speed3)
p3.forward(500)

p4 = turtle. Turtle()
p4.shape("turtle")
p4.color("blue")
p4.up()
p4.goto(0,-100)
p4.speed(speed4)
p4.forward(500)

list = [p1 , p2 , p3 , p4]

turtle.done()