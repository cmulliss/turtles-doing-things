
from turtle import *
import random
mode('logo')
shape('turtle')
color('white')
bgcolor('blue')
pensize(2)
shapesize(1)
colours = ['cyan', 'purple', 'green', "red", 'yellow', 'red', 'orange', 'pink']


#generate snowflake size using random.randint()
dFull = random.randint(50, 100)
dBranch = (dFull / 6)
dRem = (dFull / 2)

#beginning of snowflake function
def snowflake():
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

snowflake()


    
    


        
    

