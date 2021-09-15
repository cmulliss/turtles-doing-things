import tkinter as tk
import turtle

from PIL import ImageTk, Image

from pygame import mixer

root = tk.Tk()

root.title("Snake Game")
# root.state("zoomed")
root.geometry("1280x720")

# adding sound
def on_closing():
    mixer.music.stop()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
mixer.init()
mixer.music.load(
    "/Users/cherry/repos/turtles-doing-things/snake_game/sounds/untamed.mp3"
)
mixer.music.play()


dayImage = Image.open(
    "/Users/cherry/repos/turtles-doing-things/snake_game/images/day.jpg"
)
dayImage = dayImage.resize((1280, 720), Image.ANTIALIAS)
resized1 = ImageTk.PhotoImage(dayImage)

nightImage = Image.open(
    "/Users/cherry/repos/turtles-doing-things/snake_game/images/night.jpg"
)

nightImage = nightImage.resize((1280, 720), Image.ANTIALIAS)
resized2 = ImageTk.PhotoImage(nightImage)

backgroundLabel = tk.Label(root, image=resized1)
backgroundLabel.place(x=0, y=0)

# create a canvas to hold our turtle screen
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(pady=10)

# create a turtle screen, located within canvas
turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("#e6ffcc")

# create the snake head and locate on turtle screen
head = turtle.RawTurtle(turtle_screen)
head.shape("circle")
head.color("#661a00")
head.goto(0, 0)
head.direction = "stop"


root.mainloop()
