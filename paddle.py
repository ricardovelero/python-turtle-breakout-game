from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("silver")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 60
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 60
        self.goto(new_x, self.ycor())
