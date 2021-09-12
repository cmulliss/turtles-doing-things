#draws a polygon from user input

from turtle import *
mode('logo')
color('magenta')

noOfSides = int(input('How many sides would you like, enter more than 2: '))
internalAngle = 360/noOfSides

for i in range(noOfSides):
    fd(50)
    rt(internalAngle)
    print()
    
