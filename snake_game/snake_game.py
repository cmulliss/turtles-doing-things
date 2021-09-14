import tkinter as tk
import turtle

from PIL import ImageTk, Image

root = tk.Tk()

root.title("Snake Game")
# root.state("zoomed")
root.geometry("1280x720")

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


root.mainloop()
