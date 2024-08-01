import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian State Guesser")
image = "indiaMap.gif"
screen.addshape(image)
turtle.shape(image)

# used to check the coordindates of all the states

# def get_mouse_click_coor(x,y):
#    print (x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

data = pd.read_csv("28_states.csv")
states_data = data.state.to_list()

guess_state = []
while len(guess_state) < 28:
    ans_state = screen.textinput(title=f"{len(guess_state)}/28 guess the state:",
                                 prompt="Whats the another state name: ").title()

    if ans_state == "Exit":
        missing_States = []
        for states in states_data:
            if states not in guess_state:
                missing_States.append(states)
        new_Data = pd.DataFrame(missing_States)
        new_Data.to_csv("States_to_learn.csv")
        print(missing_States)
        break

    if ans_state in states_data:
        guess_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_datas = data[data.state == ans_state]
        t.goto(states_datas.x.item(), states_datas.y.item())
        t.write(states_datas.state.item(), font=("Arial", 12, "normal"))

print("Thanks for playing this game!!")
