from turtle import *

# Very pretty star with turtle hiding at end

shape("turtle")
mode("logo")
color("blue", "red")
speed(2)
begin_fill()
while True:
    forward(180)  # distance moved
    left(170)  # angle turned
    if abs(pos()) < 1:
        break
end_fill()
hideturtle()
done()

# redo this with better import and reduce screen size
