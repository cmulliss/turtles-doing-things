# Snowman with buttons, extra fingers, legs and scarf to come!

from turtle import *

#head
circle(60)
circle(-100)
penup()

#body
goto(0,-30)
pendown()
begin_fill()
circle(5)
end_fill()
penup()

#button() buttons wanted at (0,-50 -70 -90 etc)
from buttons import buttons

buttons()
    
#eyes
goto(-30, 60)
pendown()
begin_fill()
circle(5)
end_fill()
penup()

goto(30,60)
pendown()
begin_fill()
circle(5)
end_fill()
penup()

#leftarm
goto(-50,-30)
pendown()
bk(100)
lt(30)
bk(50)
penup()

#rightarm
goto(50,-30)
pendown()
fd(100)
rt(-30)
fd(50)
penup()

#smile
goto(-40,50)
pendown()
setheading(270)
circle(35,180)
penup()

#carrot nose
goto(0,40)
pendown()
color('orange')
shapesize(1,1)
begin_fill()
circle(7)
end_fill()
penup()
