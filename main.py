#TODO: Create the snake body - 3 squares
#TODO: Move the snake so that it continuously moves forward
#TODO: Control the snake to move up down left and right
import time
import turtle
from turtle import Screen
from snek_class import Snake


snake = Snake()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



game_is_on = True

screen.listen()
screen.onkey(snake.up(),"W")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

















screen.exitonclick()