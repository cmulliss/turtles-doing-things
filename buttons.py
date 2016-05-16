#button() buttons wanted at (0,-50 -70 -90 etc)
import turtle
def buttons():

    for y in range(-50, -130, -20):
        x = 0
        turtle.goto(x,y)
        turtle.pendown()   
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
