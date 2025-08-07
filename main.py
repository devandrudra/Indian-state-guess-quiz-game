import turtle
import pandas as pd

image = "Indian_map_blank_Indian_map.gif"
screen = turtle.Screen()
screen.title("India-state-guess-quizz-game")
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("indian_state_list.csv")
indian_states = data.state.to_list()
total = 1

def printer(x, y, state):
    turtle_obj = turtle.Turtle()
    turtle_obj.hideturtle()
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.write(state, font=("Arial", 16, "bold"))

print(len(indian_states))
while total <= len(indian_states):
    answer_state = screen.textinput(title = f"{total}/{len(indian_states)} corrected yet!", prompt = "enter the state name: ")
    answer_state = answer_state.title()
    if answer_state in indian_states:
        coord = data[data.state == answer_state]
        printer(int(coord.X), int(coord.Y,), answer_state)
        total += 1




screen.exitonclick()