import turtle
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE=20


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head=self.turtle_list[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)


    def add_turtle(self,position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.turtle_list.append(turtle)

    def extend(self):
        self.add_turtle(self.turtle_list[-1].position())

    def move(self):
        for turtle_index in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle_index - 1].xcor()
            new_y = self.turtle_list[turtle_index - 1].ycor()
            self.turtle_list[turtle_index].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading()!=270:
            self.head.seth(90)
    def down(self):
        if self.head.heading()!= 90:
            self.head.seth(270)
    def right(self):
        if self.head.heading()!= 180:
            self.head.seth(0)
    def left(self):
        if self.head.heading()!= 0:
            self.head.seth(180)


