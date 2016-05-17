#eyes() eyes wanted at (0,-50 -70 -90 etc)
from turtle import *
def eyes():

    for x in range(-30, 90, 60):
        y = 60
        goto(x,y)
        pendown()
        begin_fill()
        circle(5)
        end_fill()
        penup()
