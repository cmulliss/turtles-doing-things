#button() buttons wanted at (0,-50 -70 -90 etc)
from turtle import *
def buttons():

    for y in range(-50, -130, -20):
        x = 0
        goto(x,y)
        pendown()   
        begin_fill()
        circle(5)
        end_fill()
        penup()
