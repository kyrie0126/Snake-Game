from snake import Snake, Screen
import time
from scoreboard import ScoreBoard

# create snake body
snake = Snake()
screen = Screen()
# screen settings
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.title("Kyle's Snake Game")
screen.tracer(0)

# create scoreboard
scoring = ScoreBoard()

# steering mechanics
def left():
    snake.body_parts[0].setheading(180)

def right():
    snake.body_parts[0].setheading(0)

def up():
    snake.body_parts[0].setheading(90)

def down():
    snake.body_parts[0].setheading(270)


screen.listen()
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=up, key="w")
screen.onkey(fun=down, key="s")

# spawn snake
snake.spawn()

# snake does stuff!
snake.cake.create()

game_is_on = True
while game_is_on:
    snake.screen.update()
    time.sleep(.2)

    snake.body_parts_locations = []
    snake.head_location = []

    # body movement mechanics
    for i in range(len(snake.body_parts) - 1, 0, -1):
        snake.body_parts[i].goto(x=snake.body_parts[i - 1].xcor(), y=snake.body_parts[i - 1].ycor())
        snake.body_parts_locations.append(snake.body_parts[i])
    snake.body_parts[0].forward(20)
    snake.head_location.append(snake.body_parts[0].pos())

    # eating detection
    if snake.cake.food.distance(snake.body_parts[0]) < 5:
        snake.cake.food.reset()
        snake.cake.create()
        snake.grow()
        scoring.increase_score()

    # collision detection
    if snake.body_parts[0].xcor() < -300 or snake.body_parts[0].xcor() > 300 \
            or snake.body_parts[0].ycor() < -300 or snake.body_parts[0].ycor() > 300:
        scoring.reset()
        snake.reset()

    for parts in snake.body_parts_locations:
        if parts.distance(snake.body_parts[0]) < 5:
            scoring.reset()
            snake.reset()

# exit by click once dead
screen.exitonclick()

# need to add boundaries
