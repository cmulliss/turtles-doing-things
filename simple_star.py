# import turtle

# t = turtle

# for i in range(5):
#     t.fd(50)
#     t.rt(144)

# turtle.done()

from turtle import Turtle, Screen

t = Turtle()  # turtle instance creation

for i in range(5):
    t.forward(50)  # turtle instance method
    t.right(144)  # turtle instance method

screen = Screen()  # access sole screen instance
screen.mainloop()  # screen instance method
