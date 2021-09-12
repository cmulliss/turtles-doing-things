
from turtle import *
import random
mode('logo')
shape('turtle')
color('white')
bgcolor('blue')
speed(600)
pensize(2)
shapesize(1)
colours = ['cyan', 'purple', 'green', "red", 'yellow', 'red', 'orange', 'pink']


#generate snowflake size using random.randint()
dFull = random.randint(30, 100)
dBranch = (dFull / 6)
dRem = (dFull / 2)

#beginning of snowflake function
def snowflake(dFull):
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

#call snowflake function
#snowflake()

#loop to create 10 randomly sized snowflakes
for i in range(10, dFull):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
 #   snowFlakeSize = random.randint(10, 100)
    penup()
    goto(x, y)
    pendown()
    snowflake(dFull)
    


    
    


        
    

