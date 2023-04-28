from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 3
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(y=-300, x=0)
        self.x_move = self.ball_speed
        self.y_move = self.ball_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, -300)
        self.bounce_y()

    def set_speed(self, speed):
        if self.x_move < 1 or self.y_move < 1:
            self.x_move = -speed
            self.y_move = -speed
        else:
            self.x_move = speed
            self.y_move = speed
