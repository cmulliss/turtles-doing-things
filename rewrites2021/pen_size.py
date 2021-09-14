import turtle

t = turtle.Turtle()

t.pencolor("green")
for i in range(10):
    t.pensize(i)
    t.fd(20)

turtle.done()
