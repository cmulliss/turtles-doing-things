
from turtle import *
import random
mode('logo')
shape('turtle')
color('white')
bgcolor('blue')
pensize(2)
shapesize(1)
colours = ['cyan', 'purple', 'green', "red", 'yellow', 'red', 'orange', 'pink']


for i in range(6):
        fd(100)

        for i in range(6):
            color(random.choice(colours))
            bk(10)
            lt(60)
            fd(15)
            bk(15)
            rt(120)
            fd(15)
            bk(15)
            lt(60)

        bk(40)
        rt(60)


    
    


        
    

