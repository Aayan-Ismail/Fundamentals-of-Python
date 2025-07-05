import turtle
pen = turtle. Turtle()
paper = turtle. Screen()

age = int(input("enter your age: "))
name = input("Name: ")
hobby = input("Hobby: ")
fav_color =input("Favourite Color: ")
fav_food = input("Favourite Food: ")

#fancy star
i = 0
while i < 8:
    pen.forward(60)
    pen.right(135)
    i = i + 1

#movement for average star
pen.up()
pen.goto(200,200)
pen.down()
o = 0
while o < 5:
    pen.forward(80)
    pen.right(144)
    o = o + 1

#extra fancy star
pen.up()
pen.goto(-200,-200)
pen.down()
p = 0
while p < 12:
    pen.forward(100)
    pen.right(150)
    p = p + 1

turtle.done()
