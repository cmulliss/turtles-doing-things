import tkinter as tk

# our snake class is inheriting from canvas, so it is now a canvas!
class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=600, height=620, background="black", highlightthickness=0
        )


# create main app window
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

# having created our class, above, we now put it into a variable which will be an instance of our snake class. Our snake class for now is just a canvas. When we create it, we are calling the canvases constructor, setting some properties and put it into the window, using the pack method.
board = Snake()

# to run app:
root.mainloop()

# would normally to this:
# canvas = tk.Canvas()
# but we are going to be putting a lot into the canvas, so better to inherit from canvas and create our own class. So whenever we access any methods of the Snake class, we are going to access them in the canvas, unless we override them in our own class.
