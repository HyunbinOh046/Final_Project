import turtle
from turtle import Turtle, Screen

screen = Screen()
t = Turtle("turtle")
t.speed(-1)

pen = turtle.Turtle()
pen.hideturtle()

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def clickright(x, y):
    t.clear()

# Button to change color
def color_bt():
    for i in range(2):
        pen.forward(80)
        pen.left(90)
        pen.forward(30)
        pen.left(90)

# Button to change width of pen

def main():
    turtle.listen()

    t.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)

    screen.mainloop()

main()
