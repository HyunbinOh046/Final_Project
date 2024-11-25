import turtle
from turtle import Turtle, Screen

screen = Screen()
t = Turtle("turtle")
t.speed(-1)
t.shapesize(2,2,2)

#Blue Color Button
def blue_button():
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

#Red Color Button
def red_button():
    pen = turtle.Turtle()
    pen.hideturtle()
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


# Button to change width of pen

def main():
    turtle.listen()
    t.ondrag(dragging)
    blue_button()
    red_button()
    turtle.onscreenclick(clickright, 3)
    turtle.onscreenclick(color_bt, 1)
    screen.mainloop()

main()
