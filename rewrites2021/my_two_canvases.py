from turtle import TurtleScreen, RawTurtle, TK


def main():

    root = TK.Tk()
    canvas1 = TK.Canvas(root, width=1350, height=350)
    canvas2 = TK.Canvas(root, width=1350, height=350)
    canvas1.pack()
    canvas2.pack()

    screen1 = TurtleScreen(canvas1)
    screen1.bgcolor(0.80, 0.80, 1)
    screen2 = TurtleScreen(canvas2)
    screen2.bgcolor(1, 0.80, 0.80)

    k = RawTurtle(screen1)
    j = RawTurtle(screen2)

    k.color("red", (1, 0.80, 0.80))
    k.width(5)
    j.color("blue", (0.8, 0.80, 1))
    j.width(5)

    for t in k, j:
        t.speed(400)
        t.shape("turtle")

    for t in k, j:

        return "EVENTLOOP"


if __name__ == "__main__":
    main()
    TK.mainloop()
