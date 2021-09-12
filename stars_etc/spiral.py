#!/usr/bin/python
# a square spiral

from turtle import *

shape('turtle')
mode('logo')
color('magenta', 'cyan')

for n in range(10, 200, 20):
    fd(n)
    rt(90)
    fd(n)
    rt(90)
    fd(n + 10)
    rt(90)
    fd(n + 10)
    rt(90)
ht()
    
