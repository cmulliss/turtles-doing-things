from turtle import *
from random import choice

color('cyan')
colors = ['white', 'purple', 'green', 'blue', 'cyan', 'red', 'magenta']
bgcolor('grey')

# position turtle

penup()
setpos(90,0)
lt(45)
pendown()

def branch():
    for i in range(3):
        for i in range(3):
            fd(30)
            bk(30)
            rt(45)
        lt(90)
        bk(30)
        left(45)
    rt(90)
    fd(90)

for i in range(6):
    branch()
    lt(30)
    
    


        
    

