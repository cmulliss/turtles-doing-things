#!/usr/bin/python
from turtle import *
'''draws stars from input, formula
internal angle = 180 / number of points
turtle has to turn to the right such that the internal angle is
internalAngle, so has to turn 180 - internalAngle
for a 5 pointer
internal angle = 180 / 5
and therefore turn angle is
180 - 36 = 144
also
setheading is set to half the internal angle to prevent lopsidedness!
'''

shape('turtle')
mode('logo')
color('magenta', 'cyan')

points = int(input('How many points would you like on your star, enter an odd number greater than 1: ')) 

internalAngle = 180/points
turn = 180 - internalAngle
initialHeading = internalAngle/2

setheading(initialHeading)

for i in range(points):
    fd(200)
    rt(turn)
