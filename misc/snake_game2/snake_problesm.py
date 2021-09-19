import tkinter as tk
from random import randint

# import image processing classes
from PIL import Image, ImageTk

MOVE_INCREMENT = 20
MOVES_PER_SECOND = 15
GAME_SPEED = 1000 // MOVES_PER_SECOND


# our snake class is inheriting from canvas, so it is now a canvas!
# also need pack as geometry manager
class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=600, height=620, background="black", highlightthickness=0
        )
        # defining where snake is going to start,list of tuples, each containing coords for one piece of snakes body, each element 20px wide. 3 instances of the snake image. First is head, which is more to R.
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 200)
        self.score = 0
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)

        self.load_assets()
        self.create_objects()
        self.bind_all("<Key>", self.on_key_press)

        self.pack()

        self.after(GAME_SPEED, self.perform_actions)

    # first 'Image' loads the image, then 'ImageTK' creates a photo version
    def load_assets(self):
        try:
            self.snake_body_image = Image.open("misc/snake_game2/assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("misc/snake_game2/assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            print(error)
            root.destroy()
            raise

    # 'create_objects' to place in window
    # 'create_image' place the objects in the window
    # destructure with the *
    def create_objects(self):
        # create text wherever we want it
        self.create_text(
            35,
            12,
            text=f"Score: {self.score}",
            tag="score",
            fill="#fff",
            font=("TkDefaultFont", 16),
        )

        for x_position, y_position in self.snake_positions:
            self.create_image(
                x_position, y_position, image=self.snake_body, tag="snake"
            )
        self.create_image(*self.food_position, image=self.food, tag="food")
        # creating boundaries, so know when going to crahs
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    # moving the snake from initial position, and destructuring

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]
        # need to make snake listen for new position
        if self.direction == "Left":
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == "Right":
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)

        # move head then copy it and chop off last element of tail
        self.snake_positions = [new_head_position] + self.snake_positions[:-1]
        # find all the elements with tag 'snake' and all positions, zip fn entertwines element and postion and produces tuples for each postion
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    # return means we no longer call self.after, so not going to perform actions.
    def perform_actions(self):
        if self.check_collisions():
            return

        self.move_snake()
        self.after(GAME_SPEED, self.perform_actions)

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("misc/snake_game2/assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("misc/snake_game2/assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            root.destroy()
            raise

    def create_objects(self):
        self.create_text(
            35, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=10
        )

        for x_position, y_position in self.snake_positions:
            self.create_image(
                x_position, y_position, image=self.snake_body, tag="snake"
            )

        self.create_image(*self.food_position, image=self.food, tag="food")
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    # start by getting the parent head of snake
    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]
        # check snake not colliding with sides, not eating itself
        return (
            head_x_position in (0, 600)
            or head_y_position(20, 620)
            or (head_x_position, head_y_position) in self.snake_positions[1:]
        )

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            self.create_image(
                *self.snake_positions[-1], image=self.snake_body, tag="snake"
            )
            self.food_position = self.set_new_food_position()
            self.coords(self.find_withtag("food"), *self.food_position)

            score = self.find_withtag("score")
            self.itemconfigure(score, text=f"Score: {self.score}", tag="score")

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game over! You scored {self.score}!",
            fill="#fff",
            font=14,
        )

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]

        if self.direction == "Left":
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == "Right":
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    # whenever a key is pressed going to run this method
    # starts by gettig the new direction, e.keysym
    # whenever we call a fn bound to any key then also gives us an event
    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def perform_actions(self):
        if self.check_collisions():
            self.end_game()

        self.check_food_collision()
        self.move_snake()

        self.after(GAME_SPEED, self.perform_actions)

    def set_new_food_position(self):
        while True:
            x_position = randint(1, 29) * MOVE_INCREMENT
            y_position = randint(3, 30) * MOVE_INCREMENT
            food_position = (x_position, y_position)

            if food_position not in self.snake_positions:
                return food_position


root = tk.Tk()
root.title("Snake")
root.resizable(False, False)
root.tk.call("tk", "scaling", 4.0)


# having created our class, above, we now put it into a variable which will be an instance of our snake class. Our snake class for now is just a canvas. When we create it, we are calling the canvases constructor, setting some properties and put it into the window, using the pack method.
# instantiate an object of our Snake class and call it board
board = Snake()

# to run app:
root.mainloop()

# would normally to this:
# canvas = tk.Canvas()
# but we are going to be putting a lot into the canvas, so better to inherit from canvas and create our own class. So whenever we access any methods of the Snake class, we are going to access them in the canvas, unless we override them in our own class.

# 2 methods for adding images to our Canvas. Ist to load images into our app, 2nd to place them on the Canvas.
# Once we've processed our images in the try block, we can call the load_assets method inside of __init__.
