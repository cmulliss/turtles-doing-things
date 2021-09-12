# Multiple snowflakes

from turtle import *
import random
mode('logo')
shape('turtle')
color('white')
bgcolor('blue')
pensize(2)
shapesize(1)
speed(600)
colours = ['cyan', 'white', 'green', "red", 'yellow', 'red', 'orange', 'pink']

#beginning of snowflake function
def snowflake(flakeSize):
    dFull = random.randint(4, 80)
    dBranch = (dFull / 6)
    dRem = (dFull / 2)
    for i in range(6):
        fd(dFull)

        for i in range(3):
            color(random.choice(colours))
            bk(dBranch)
            lt(60)
            fd(dBranch)
            bk(dBranch)
            rt(120)
            fd(dBranch)
            bk(dBranch)
            lt(60)

        bk(dRem)
        rt(60)
#end of snowflake function
        
#loop to create multiple snowflakes in different locations
for i in range(15):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    flakeSize = random.randint(1, 100)
    penup()
    goto(x, y)
    pendown()
    snowflake(flakeSize)





