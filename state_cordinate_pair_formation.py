import turtle
import pandas as pd
screen = turtle.Screen()
image = "Indian_map_blank_Indian_map.gif"
screen.addshape(image)
screen.title("India-state-quiz-game")
turtle.shape(image)

indian_states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
state_index = 0
indian_state_file = pd.read_csv("indian_state_list.csv")
def get_mouse_click_coor(x, y):
    global state_index;
    state = indian_states[state_index]
    print(f"{x},{y}")
    data = {
        'state' : state,
        'x': x,
        'y':y
    }
    df = pd.DataFrame([data])
    df.to_csv("indian_state_list.csv", mode = 'a',  index=False, header=False)
    state_index += 1
    if state_index >= len(indian_states):
        screen.bye()
    else:
        ask_next_state()


def ask_next_state():
    state = indian_states[state_index]
    screen.title(f"Click for: {state}")
    turtle.onscreenclick(get_mouse_click_coor)

ask_next_state()

screen.mainloop()


screen.exitonclick()

# git config --global user.name "Nitkarsh Mishra"
# git config --global user.email "nitkarsh123@gmail.com"
