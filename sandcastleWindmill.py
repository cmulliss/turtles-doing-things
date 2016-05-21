#sandcastle windmill

from turtle import *
from random import choice
mode('logo')
colours = ['cyan', 'purple', 'green', 'red', 'blue', 'red', 'orange']
shape('square')
color('purple', 'green')

pensize(4)
pencolor('brown')
goto(0,-300)
fd(300)
pensize(1)


for i in range(10):
    for i in range(2):
        begin_fill()
        fd(100)
        rt(60)
        fd(100)
        rt(120)
        end_fill()
    rt(36)   
    color(choice(colours))




