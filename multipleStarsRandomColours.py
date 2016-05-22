# Multiple stars in different colours and sizes

from turtle import *
import random
mode('logo')
shape('turtle')
color('white')
bgcolor('blue')
pensize(2)
shapesize(1)
speed(600)
colours = ['cyan', 'white', 'green', "red", 'yellow', 'red', 'orange', 'pink','purple', 'magenta','grey', 'turquoise' ]

#beginning of star function
def star(starSize):
    color(random.choice(colours))
    points = (5)
    internalAngle = 180/points
    turn = 180 - internalAngle
    initialHeading = internalAngle/2

    setheading(initialHeading)

    for i in range(points):
        fd(starSize)
        rt(turn)
       
#end of star function
        
#loop to create multiple stars in different locations
for i in range(30):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    starSize = random.randint(4, 100)
    penup()
    goto(x, y)
    pendown()
    star(starSize)
hideturtle()





