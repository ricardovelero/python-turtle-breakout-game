import turtle as tr
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from lifes import Lifes
import time

screen = tr.Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()

lifes = Lifes()

ball = Ball()

paddle = Paddle((0, -375))

bricks = Bricks()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 385:
        ball.bounce_y()
    elif ball.xcor() < -490 or ball.xcor() > 480:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -355:
        ball.bounce_y()

    # Detect paddle miss
    if ball.distance(paddle) > 10 and ball.ycor() < -400:
        ball.reset_position()
        lifes.decrease_life()
        if lifes.lifes < 1:
            game_is_on = False

    # Detect brick hit
    hit_brick = bricks.detect_hit(ball)
    if hit_brick:
        scoreboard.point()
        match hit_brick:
            case "green":
                ball.set_speed(5)
            case "yellow":
                ball.set_speed(7)
            case "orange":
                ball.set_speed(9)
            case "red":
                ball.set_speed(11)
            case _:
                ball.set_speed(3)
        ball.bounce_y()
        ball.bounce_x()


tr.mainloop()
