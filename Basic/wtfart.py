from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.pencolor('#32c18f')


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)


screen.bgcolor("#212121")
screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Left", fun=move_left)
screen.exitonclick()