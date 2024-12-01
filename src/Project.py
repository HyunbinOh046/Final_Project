import turtle
from turtle import Turtle, Screen

screen = Screen()
t = Turtle("turtle")
t.speed(-1)
t.shapesize(2,2,2)

# Drawing Buttons
def buttons():
    pen = turtle.Turtle()
    pen.hideturtle()

    #Blue color button
    pen.fillcolor("blue")
    pen.begin_fill()

    pen.up()
    pen.forward(260)
    pen.down()

    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(30)
        pen.left(90)

    pen.penup()
    pen.goto(1,1)
    pen.end_fill()
    
    pen.penup
    pen.forward(350)
    pen.pendown

    #Red Color Button
    pen.fillcolor("red")
    pen.begin_fill()

    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(30)
        pen.left(90)

    pen.penup()
    pen.goto(0,0)
    pen.end_fill()

    pen.penup
    pen.forward(260)
    pen.right(90)
    pen.forward(40)
    pen.left(90)
    pen.pendown

    # Green Color button
    pen.fillcolor('green')
    pen.begin_fill()

    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(30)
        pen.left(90)

    pen.penup()
    pen.goto(0,0)
    pen.end_fill()

    # Yellow Color Buton
    pen.penup
    pen.forward(350)
    pen.right(90)
    pen.forward(40)
    pen.left(90)
    pen.pendown

    pen.fillcolor('yellow')
    pen.begin_fill()

    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(30)
        pen.left(90)
    
    pen.penup()
    pen.goto(0,0)
    pen.end_fill()


class slider(Turtle):
    def __init__(self, x, y, c):
        Turtle.__init__(self)
        self.shape('square')
        self.shapesize(2,2,2)
        self.pensize(10)
        self.speed(0)
        self.up()
        self.color(c)
        self.goto(x, -120)
        self.down()
        self.goto(x, 120)
        self.ondrag(self.drag)

    def drag(self, x, y):
        if (y<=120 and y >= -120):
            self.sety(y)
        if (y > -120 and y < -80):
            t.pensize(1) 
        elif (y > -80 and y < -40):
            t.pensize(2)
        elif (y > -40 and y < 0):
            t.pensize(3)
        elif (y > 0 and y < 40):
            t.pensize(4)
        elif (y > 40 and y < 80):
            t.pensize(5)
        else:
            t.pensize(6) 


# Turtle to draw
def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

# Reset the color and pensize
def clickright(x, y):
    t.clear()
    t.pencolor('black')
    t.pensize(1)

# Button to change color
def color_bt(x, y):
    if x > 260 and x < 340 and y > 0 and y < 30:
        t.pencolor("blue")
    if x > 350 and x < 430 and y > 0 and y < 30:
        t.pencolor("red")
    if x > 260 and x < 340 and y > -40 and y < 0:
        t.pencolor("green")
    if x > 350 and x < 430 and y > -40 and y < 0:
        t.pencolor("yellow")


def main():
    turtle.listen()
    t.ondrag(dragging)
    buttons()
    slider(600, 0, 'black')
    turtle.onscreenclick(clickright, 3)
    turtle.onscreenclick(color_bt, 1)
    screen.mainloop()

main()
