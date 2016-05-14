from turtle import *
whatShape = input('Please enter a shape either a circle square, triangle or hexagon > ')

mode('logo')
color('blue', 'red')
   
if whatShape == 'circle':
    
        radius = int(input('Please enter a radius > '))
        circle(radius)
elif whatShape == 'square':
    side = int(input('Please enter a side length > '))
    for i in range (4):
        fd(side)
        rt(90)
elif whatShape == 'triangle':
    side = int(input('Please enter a side length > '))
    for i in range (3):
        fd(side)
        rt(120)
elif whatShape == 'hexagon':
    side = int(input('Please enter a side length > '))
    for i in range (6):
        fd(200)
        rt(60)

else:
    print('Oops, not sure what shape you mean?')
    
        
