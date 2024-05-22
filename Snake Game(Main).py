

from Snake import Snake
from Food import Food
from scoreboard_snake_game import Scoreboard
# import os
from turtle import *
import time

num_of_collision = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()


screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

# step 2: How to move the snake...(Animating the snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
# Detecting the collision with food:
    if snake.head.distance(food) < 15:
        num_of_collision += 1
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
# Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


#     Detect collision of tail
#     If head collides with any segment in the tail then its game over

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()









