import turtle
pen = turtle. Turtle()



for i in range(4):
    pen.forward(50)
    pen.right(90)

pen.up()
pen.goto(200,200)
pen.down()

for o in range (8):
    pen.right(45)
    pen.forward(50)


for l in range(3):
    answer = input("what is the object that is drawn?, you have 3 tries to answer correctly. ")

    if (answer == "square"):
        print("good job!")

    else:
        print("you are wrong")

    answer2 = input("what is the next object shown? ")

    if (answer2 == "octogon"):
        print("correct!")

    else:
        print("incorrect ")
    
    