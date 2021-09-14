import tkinter as tk
from turtle import RawTurtle, TurtleScreen


def cleanup():
    """hide the turtles"""

    arc1.hideturtle()
    arc2.hideturtle()


def moveTurtles(rangevar, radius, extent, decrease):
    """animate the turtles"""

    for _ in range(rangevar):
        arc1.circle(-radius, extent=extent)
        arc2.circle(-radius, extent=extent)
        radius -= decrease


def setTurtle(turtle, x, y, heading, pensize, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.setheading(heading)
    turtle.pensize(pensize)
    turtle.pencolor(color)


def draw():
    # set variables
    rangevar = 200
    radius = 200
    decrease = 1
    extent = 2

    screen.tracer(False)  # turn off animation while drawing outline

    # setup and draw the outline
    setTurtle(arc1, 0, 200, 0, 40, "grey")
    setTurtle(arc2, 14, -165, 180, 40, "grey")
    moveTurtles(rangevar, radius, extent, decrease)

    screen.tracer(True)  # turn animation back on for the following

    # setup and animate the logo
    setTurtle(arc1, 0, 200, 0, 20, "black")
    setTurtle(arc2, 14, -165, 180, 20, "black")
    moveTurtles(rangevar, radius, extent, decrease)


# main program

window = tk.Tk()
window.title("Top 10's")

canvas = tk.Canvas(master=window, width=500, height=500)
canvas.pack()

screen = TurtleScreen(canvas)

arc1 = RawTurtle(screen)
arc1.speed("fastest")

arc2 = RawTurtle(screen)
arc2.speed("fastest")

draw()
cleanup()
