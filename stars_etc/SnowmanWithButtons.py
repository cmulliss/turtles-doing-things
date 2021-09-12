# Snowman with scarf to be added later (possibly)!
# Added path to my local modules
import sys
sys.path.append('/Users/cherry/Desktop/repos/turtles-doing-things/myModules')
	
from turtle import *
from buttons import buttons
from eyes import eyes

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

#button() buttons required at (0,-50 -70 -90 etc)
buttons()

#eyes() eyes required at (-30, 30)
eyes()

#leftarm
goto(-50,-30)
pendown()
bk(70)
lt(30)
bk(50)
fd(50)
rt(60)
bk(50)
penup()

#rightarm
goto(50,-30)
pendown()
fd(70)
rt(-30)
fd(50)
bk(50)
rt(60)
fd(50)
penup()

#smile
goto(-35,50)
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
