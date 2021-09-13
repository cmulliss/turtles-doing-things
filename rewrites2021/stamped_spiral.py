import turtle

s = turtle.Screen()
s.bgcolor("pink")
s.title("Turtle spiral")
# s.setup(width=650, height=650)
s.setup(width=0.2, height=0.3)

t = turtle.Turtle()
t.shape("turtle")
t.color("red")


t.pu()
size = 20

for i in range(30):
    t.stamp()
    size = size + 3
    t.fd(size)
    t.rt(24)

# s.mainloop()
s.exitonclick()
