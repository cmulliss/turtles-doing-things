import turtle
t = turtle

t.mode('logo')
t.shape('turtle')
t.speed(3)
t.color('magenta', 'cyan')
for i in range (4):
    t.fd(200)
    t.rt(90)
  
t.goto(200,200)
t.goto(0,200)
t.goto(200,0)
t.rt(720)

t.speed(1)
t.penup()
t.goto(-200, -200)
t.pendown()
t.color('green', 'red')
for i in range (4):
    t.fd(200)
    t.rt(90)
t.goto(0,0)
t.goto(0,0)
t.goto(-200,0)
t.goto(0,-200)


