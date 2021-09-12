import turtle

star = turtle

# Very pretty star with turtle hiding at end

star.shape("turtle")
star.mode("logo")
star.color("blue", "red")
star.speed(2)
star.begin_fill()
while True:
    star.forward(180)  # distance moved
    star.left(170)  # angle turned
    if abs(star.pos()) < 1:
        break
star.end_fill()
star.hideturtle()
star.exitonclick()

# redo this with better import and reduce screen size
