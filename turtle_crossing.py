import time
import random
from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

# Player (the turtle)
player = Turtle("turtle")
player.color("black")
player.penup()
player.goto(0, -280)
player.setheading(90)

# Scoreboard
level = 1
scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-280, 260)
scoreboard.write(f"Level: {level}", align="left", font=("Arial", 16, "normal"))

# Cars
cars = []
CAR_SPEED = 5

def create_car():
    new_car = Turtle("square")
    new_car.shapesize(stretch_wid=1, stretch_len=2)
    new_car.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
    new_car.penup()
    new_car.goto(300, random.randint(-250, 250))
    cars.append(new_car)

def move_cars():
    for car in cars:
        car.backward(CAR_SPEED)

# Player movement
def move_up():
    player.forward(20)

screen.listen()
screen.onkey(move_up, "Up")

# Game loop
game_is_on = True
car_timer = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars randomly
    car_timer += 1
    if car_timer % 6 == 0:
        create_car()

    # Move cars
    move_cars()

    # Detect collision with cars
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False
            game_over = Turtle()
            game_over.hideturtle()
            game_over.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    # Check if player reached the top
    if player.ycor() > 280:
        player.goto(0, -280)
        level += 1
        CAR_SPEED += 2
        scoreboard.clear()
        scoreboard.write(f"Level: {level}", align="left", font=("Arial", 16, "normal"))

screen.exitonclick()
