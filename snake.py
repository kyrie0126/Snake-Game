from turtle import Turtle, Screen
from food import SnakeFood


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.cake = SnakeFood()
        self.body_parts = []
        self.body_parts_locations = []
        self.head_location = []

    def spawn(self):
        """Reset to 3 blocks at origin"""
        self.body_parts = []
        for i in range(0, 3):
            self.body = Turtle()
            self.body.penup()
            self.body.shape("square")
            self.body.color("white")
            self.body.goto(int(0 - 20 * i), int(0))
            self.body_parts.append(self.body)


    def grow(self):
        for i in range(0, 3):
            self.body = Turtle()
            self.body.penup()
            self.body.shape("square")
            self.body.color("white")
            last_piece = self.body_parts[-1]
            self.body.goto(last_piece.pos())
            self.body_parts.append(self.body)

    def tail_collision(self):
        if any(item in self.head_location for item in self.body_parts_locations):
            return "collision"

    def reset(self):
        for segment in self.body_parts:
            segment.hideturtle()
        self.spawn()
        self.head_location = []


