from turtle import Turtle


class Lifes(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lifes = 4
        self.update_lifes()

    def update_lifes(self):
        self.clear()
        self.goto(-450, 350)
        self.write(self.lifes, align="center",
                   font=("Courier", 40, "normal"))

    def decrease_life(self):
        self.lifes -= 1
        if self.lifes < 3:
            self.color("orange")
        elif self.lifes < 2:
            self.color("red")
        self.update_lifes()
