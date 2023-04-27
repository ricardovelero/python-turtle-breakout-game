from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.tracer(0.5)

scoreboard = Scoreboard()

ball = Ball()

paddle = Paddle((0, -350))

bricks = Bricks()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 385:
        ball.bounce_y()
    elif ball.xcor() < -490 or ball.xcor() > 480:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -325:
        ball.bounce_y()

    # Detect paddle miss
    if ball.ycor() < -385:
        ball.reset_position()

    # Detect brick hit
    hit_brick = bricks.detect_hit(ball)
    if hit_brick:
        scoreboard.point()
        ball.bounce_y()

screen.exitonclick()
