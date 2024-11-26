import turtle
from turtle import Turtle, Screen

screen = Screen()
t = Turtle("turtle")
t.speed(-1)
t.shapesize(2,2,2)

#Blue Color Button
def button():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.fillcolor("blue")
    pen.begin_fill()

    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(30)
        pen.left(90)

    pen.penup()
    pen.goto(7,6)
    pen.end_fill()
    
    pen.penup
    pen.forward(100)
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
    pen.goto(7,6)
    pen.end_fill()


def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def clickright(x, y):
    t.clear()
    t.pencolor('black')

# Button to change color
def color_bt(x, y):
    if x > 0 and x < 81 and y > 0 and y < 30:
        t.pencolor("blue")
    if x > 100 and x < 180 and y > 0 and y < 30:
        t.pencolor("red")


# Button to change width of pen

def main():
    turtle.listen()
    t.ondrag(dragging)
    button()
    turtle.onscreenclick(clickright, 3)
    turtle.onscreenclick(color_bt, 1)
    screen.mainloop()

main()
