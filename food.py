from turtle import Turtle
import random


class SnakeFood:
    def __init__(self):
        self.food = Turtle()
        self.food.penup()
        self.location = []

    def create(self):
        self.location = []
        num_range = range(-280, 281, 20)
        x = random.choice(num_range)
        y = random.choice(num_range)
        self.food.goto(x, y)
        self.food.hideturtle()
        self.food.dot(20, "blue")
        self.location.append(self.food.pos())

