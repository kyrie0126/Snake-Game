from turtle import Turtle, Screen
import time
from food import SnakeFood


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.cake = SnakeFood()
        self.body = Turtle()
        self.body_parts = []
        self.body_parts_locations = []
        self.head_location = []
        self.score = 0

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

    def left(self):
        """Left turn logic used in cont_move."""
        self.body_parts[0].left(90)

    def right(self):
        """Right turn logic used in cont_move."""
        self.body_parts[0].right(90)

    def eat_monitor(self):
        snake_location_reformat = list(self.head_location)[0]
        print(snake_location_reformat)
        cake_location_reformat = list(self.cake.location)[0]
        print(cake_location_reformat)
        print(self.head_location)
        print(self.body_parts_locations)
        if snake_location_reformat == cake_location_reformat:
            print("eat!!!")
            self.score += 1
            print(self.score)
            self.cake.food.clear()
            self.grow()
            self.grow()
            self.grow()
            self.cake.create()

    def grow(self):
        self.body = Turtle()
        self.body.penup()
        self.body.shape("square")
        self.body.color("white")
        last_piece = self.body_parts[-1].pos()
        self.body.goto(last_piece)
        self.body_parts.append(self.body)

    def tail_collision(self):
        if any(item in self.head_location for item in self.body_parts_locations):
            return "collision"



    def primary_mechanics(self):
        """Initialize body part following rules and constant motion"""
        game_is_on = True
        self.cake.create()
        while game_is_on:
            self.screen.update()
            time.sleep(.5)
            self.screen.listen()
            self.screen.onkey(fun=self.left, key="a")
            self.screen.onkey(fun=self.right, key="d")
            self.body_parts_locations = []
            for i in range(len(self.body_parts) - 1, 0, -1):
                self.body_parts[i].goto(x=self.body_parts[i - 1].xcor(), y=self.body_parts[i - 1].ycor())
                self.body_parts_locations.append(self.body_parts[i].pos())
            self.body_parts[0].forward(20)
            self.head_location = []
            self.head_location.append(self.body_parts[0].pos())
            self.eat_monitor()
            self.screen.title(titlestring=f"Score: {self.score}")
            if self.tail_collision() == "collision":
                self.screen.title(titlestring=f"Your final score: {self.score}")
                self.body_parts[0].color("red")
                self.body_parts[0].write(arg="dead lol", font=('gothic', 50, 'bold'))
                game_is_on = False





