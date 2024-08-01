from turtle import Turtle, Screen
import random

tim = Turtle()

directions = [90, 180, 270, 360]


def randomcolour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_choice = (r, g, b)
    return random_choice


tim.speed("fastest")


for i in range(40):
    tim.circle(100)
    tim.right(10)
    tim.color(randomcolour())



screen = Screen()

screen.exitonclick()
