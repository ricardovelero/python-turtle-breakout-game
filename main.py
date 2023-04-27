from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()

paddle = Paddle((0, 350))

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")


screen.exitonclick()
