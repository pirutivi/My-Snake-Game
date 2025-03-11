import turtle
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        score.game_over()

    for turtle in snake.turtle_list[1:]:
        if snake.head.distance(turtle)<10:
            game_on=False
            score.game_over()


screen.exitonclick()