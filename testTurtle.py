from turtle import *

mode('logo')
shape('turtle')
speed(5)
color('magenta', 'cyan')
for i in range (4):
    fd(200)
    rt(90)
  
goto(200,200)
goto(0,200)
goto(200,0)
rt(720)

penup()
goto(-200, -200)
pendown()
color('green', 'red')
for i in range (4):
    fd(200)
    rt(90)
goto(0,0)
goto(0,0)
goto(-200,0)
goto(0,-200)


