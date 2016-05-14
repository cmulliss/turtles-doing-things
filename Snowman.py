'''So that's one way to draw a snowman :)
I can see that the buttons should be possible with a loop of some kind, will
work on this soon '''
from turtle import *

circle(60)
circle(-100)
penup()

goto(0,-30)
pendown()
begin_fill()
circle(5)
end_fill()
penup()

#buttons

goto(0,-50)
pendown()
begin_fill()
circle(5)
end_fill()
penup()

goto(0,-70)
pendown()
begin_fill()
circle(5)
end_fill()
penup()

goto(0,-90)
pendown()
begin_fill()
circle(5)
end_fill()
penup()

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
