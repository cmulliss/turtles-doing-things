#!/usr/bin/python
print('This will draw a star')
from turtle import *

shape('turtle')
mode('logo')
setheading(18)  # to prevent lopsidededness
color('red', 'yellow')

points = int(input('How many points? '))

for i in range(points):
    fd(200)
    rt(144)
