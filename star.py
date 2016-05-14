#coloured turtle drawing 5 point star
import turtle

turtle.shape('turtle')
turtle.color('magenta', 'cyan')
speedy = turtle.Turtle()
begin_fill()
while true:
    for i in range(5):
        speedy.forward(100)
        speedy.right(60)
        speedy.forward(100)
        speedy.right(120)
        speedy.right(36)
end_fill()
done()



