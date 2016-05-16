#snowflake.py from www.raspberrypi.org
#with ammendments and gross liberties taken
import turtle as t
import random as r

colours = ['cyan', "purple", "green", "red", "blue", "red", "orange"]
speedy = t.Turtle()
speedy.shape('turtle')
speedy.color('blue', 'green')

for i in range(10):
    for i in range(2):
        speedy.forward(100)
        speedy.right(60)
        speedy.forward(100)
        speedy.right(120)
    speedy.right(36)   
    speedy.color(r.choice(colours))



