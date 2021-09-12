from turtle import *

mode('logo')
shape('turtle')
speed(5)
color('red', 'blue')

#draws rectangle
for i in range (4):
    fd(200)
    rt(90)

#draws roof
penup()
goto(0,200)
pendown()
rt(60)
goto(100,300)
rt(60)
goto(200,200)
penup()

#resizes turtle and changes his fill colour
shapesize(5,5)
color('red', 'orange')
goto(100,100)
rt(240)
width(200)
