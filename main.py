from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()

screen.exitonclick()
