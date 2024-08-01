from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.pencolor('#32c18f')

screen = Screen()
screen.bgcolor("#212121")
def square():
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)

tim.speed(1000)

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

















screen.exitonclick()
