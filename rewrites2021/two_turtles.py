# Set up the window and its attributes
import turtle

s = turtle.Screen()
s.bgcolor("pink")

# create tess and set some attributes
t = turtle.Turtle()
t.shape("turtle")
t.color("hotpink")
t.pensize(5)
t.pencolor("blue")

# create alex, who is a second turtle object
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("green")
t2.pensize(2)
t2.pencolor("purple")
t2.hideturtle()


# Let t draw a star
for i in range(5):
    t.forward(100)
    t.right(144)


# t2, set starting postion
t2.showturtle()
t2.penup()
t2.goto(100, 100)
t2.pendown()

# let t2 draw a triangle
for i in range(4):
    t2.fd(200)
    t2.lt(120)

s.exitonclick()
