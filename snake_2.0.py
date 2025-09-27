import turtle
import random

def go_up():
    snake.setheading(90)

def go_down():
    snake.setheading(270)

def go_right():
    snake.setheading(0)

def go_left():
    snake.setheading(180)

def move():
    if snake.setheading(go_up):
        y = snake.ycor()
        snake.sety(y + 10)
    
    elif snake.setheading(go_down):
        y = snake.ycor()
        snake.sety(y - 10)
    
    elif snake.setheading(go_right):
        x = snake.xcor()
        snake.setx(x + 10)

    elif snake.setheading(go_left):
        x = snake.xcor()
        snake.setx(x - 10)

score = 0

segments = []

paper = turtle. Screen()
snake = turtle. Turtle()
snake.shape("triangle")
snake.color("green")

food = turtle. Turtle()
food.shape("circle")
food.color("red")

pen = turtle. Turtle()
pen.penup()
pen.goto(-100,-400)
pen.hideturtle()
pen.write("The current score is ", score, font=("Georgian", 100, "bold") )

paper.listen()

paper.onkeypress(go_up,"w")
paper.onkeypress(go_down,"s")
paper.onkeypress(go_right,"d")
paper.onkeypress(go_left,"a")


while True:
    paper.update()
    move()
    if snake.distance(food) < 20:
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        food.penup()
        food.goto(x,y)
        food.pendown()

        new_segment = turtle. Turtle()
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        score += 1

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)




#paper.mainloop()

# set up the screen
win = turtle.Screen()
win.title("Aayan's snake game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.setheading = "stop"

# Main game loop
while True:
    win.update()

import turtle
import time
delay=0.1
# Main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)

    def move():
        if head.setheading == "up":
            y = head.ycor() 
            head.sety(y + 20)
    
        if head.setheading == "down":
            y = head.ycor() 
            head.sety(y - 20)
    
        if head.setheading == "right":
            x = head.xcor() 
            head.setx(x + 20)
    
        if head.setheading == "left":
            x = head.xcor() 
            head.setx(x - 20)

    def go_up():
        if head.setheading != "down":
            head.setheading = "up"
 
    def go_down():
        if head.setheading != "up":
            head.setheading = "down"
 
    def go_right():
        if head.setheading != "left":
            head.setheading = "right"
    
    def go_left():
        if head.setheading != "right":
            head.setheading = "left"

import turtle
import time, random

sc=turtle.Screen()
sc.bgcolor('black')

delay=0.1
segments=[]


score = 0
highscore=0

#snake
snake=turtle.Turtle()
snake.shape('square')
snake.color('blue')
snake.penup()
snake.goto(0,100)
# snake.direction='stop'

#moving functions
def move():
  if (snake.setheading =='up') :
    y = snake.ycor()
    snake.sety(y+20)
  if snake.setheading =='down':
    y = snake.ycor()
    snake.sety(y-20)
  if snake.setheading =='right':
    x = snake.xcor()
    snake.setx(x+20)
  if snake.setheading =='left':
    x = snake.xcor()
    snake.setx(x-20)

#linking with functions
def go_up():
  snake.setheading='up'
def go_down():
  snake.setheading='down'
def go_right():
  snake.setheading='right'
def go_left():
  snake.setheading='left'

#linking with keys
sc.listen()
sc.onkey(go_up,'up')
sc.onkey(go_down,'down')
sc.onkey(go_right,'right')
sc.onkey(go_left,'left')

#food
food = turtle.Turtle()
food.shape('arrow')
food.color('yellow')
food.penup()
food.goto(100,100)

#pen
pen = turtle.Turtle()
pen.color('green')
pen.penup()
pen.goto(50,170)
pen.hideturtle()
pen.write('Score: 0, High Score:0', align='center',font=('Times New Roman',5,'normal'))

while True:
  sc.update()
  move()
  time.sleep(delay)

  if snake.distance(food)<20:
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    food.penup()
    food.goto(x,y)
    food.pendown()

    newSegment = turtle.Turtle()
    newSegment.shape('square')
    newSegment.color('red')
    newSegment.penup()
    segments.append(newSegment)
    score+=1

    if score>highscore:
      highscore=score
    pen.clear()
    pen.write('Score: {}, High Score: {}'.format(score,highscore), align='center',font=('Times New Roman',30,'normal'))

  for i in range(len(segments)-1,0,-1):
    x = segments[i-1].xcor()
    y = segments[i-1].ycor()
    segments[i].goto(x,y)

  if len(segments)>0:
    x = snake.xcor()
    y = snake.ycor()
    segments[0].goto(x,y)


turtle.done() 
