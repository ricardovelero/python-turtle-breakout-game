from turtle import Turtle

COLORS = ["blue", "green", "yellow", "orange", "red"]


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        for i in range(0, len(COLORS)):
            for x_offset in range(0, 10):
                new_brick = Turtle(shape="square")
                new_brick.shapesize(
                    stretch_wid=3, stretch_len=4.8)
                new_brick.penup()
                new_brick.color(COLORS[i])
                pos_x = -448 + x_offset * 100
                pos_y = -10 + i * 63
                new_brick.goto(x=pos_x, y=pos_y)
                self.bricks.append(new_brick)

    def detect_hit(self, ball):
        for brick in self.bricks:
            if brick.distance(ball) < 55:
                brick.hideturtle()
                brick.setx(-1000)
                return brick.color()[0]
