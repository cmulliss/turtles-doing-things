from turtle import *
import turtle

t = turtle


mode("logo")
shape("turtle")
speed(5)
color("red", "blue")
for i in range(4):
    t.stamp()
    t.fd(200)
    t.stamp()
    t.rt(90)

goto(200, 200)
goto(0, 200)
goto(200, 0)

rt(720)

turtle.exitonclick()
# turtle.done()
