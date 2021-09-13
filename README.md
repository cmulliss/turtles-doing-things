# Python

## Turtle and turtle

* turtle is the package or library and Turtle() class constructor method used to instantiate the class

* turtle is the name of the package while Turtle is the name of the class.

* turtle is a method which contains a class which is noble Turtle

* from turtle import Turtle, Screen

## screen size

* The screensize() method sets the amount of area the turtle can roam, but doesn't change the screen size (despite the name), just the scrollable area. Also, to simplify your code, speed it up and produce a more detailed result, I suggest the following rework:

```python 

from turtle import Screen, Turtle

WIDTH, HEIGHT = 360, 360

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

def scalePoint(n, start1, stop1, start2, stop2):
    return (n - start1) * (stop2 - start2) / (stop1 - start1)  + start2

screen.tracer(False)

for x in range(WIDTH):
    real = scalePoint(x, 0, WIDTH, -2, 2)

    for y in range(HEIGHT):

        imaginary = scalePoint(y, 0, HEIGHT, -2, 2)

        c = complex(real, imaginary)

        z = 0j

        color = 'pink'

        for _ in range(100):
            if abs(z) >= 16.0:
                break
```

## ending program

* using:
s = turtle.Screen()
s.exitonclick()

## Setting the size of turtle screen

```python
import turtle

s = turtle.Screen()
s.bgcolor("pink")
s.title("Turtle spiral")
s.setup(width=650, height=650)

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
```

or can use a fraction:
s.setup(width=0.5, height=0.5)
