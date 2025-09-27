import turtle
pen = turtle. Turtle()
paper = turtle. Screen()

import random

colour = ["red" , "orange" , "yellow" , "green" , "gray" , "navy" , "black" , "ivory"]

def changecolour(x,y):
  
  randomcolour = random.choice(colour)
  paper.bgcolor(randomcolour)

paper.onscreenclick(changecolour)

turtle.done()