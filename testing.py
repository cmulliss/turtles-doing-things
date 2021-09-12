from turtle import *

t = Turtle


mode("logo")
shape("turtle")
color("white")
bgcolor("blue")
pensize(2)
shapesize(1)

color("blue", "red")

# do it 4 times

for i in range(4):
    t.fd(100)
    t.rt(90)
