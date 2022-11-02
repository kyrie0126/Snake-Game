from snake import Snake

# create snake body
snake = Snake()

# screen settings
snake.screen.setup(width=620, height=620)
snake.screen.bgcolor("black")
snake.screen.title("Kyle's Snake Game")
snake.screen.tracer(0)

# spawn snake
snake.spawn()

# snake does stuff!
snake.primary_mechanics()

# exit by click once dead
snake.screen.exitonclick()

# need to add boundaries
