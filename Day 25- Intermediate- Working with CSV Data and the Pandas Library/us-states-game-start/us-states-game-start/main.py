import turtle
import pandas as pd
FONT = ("Courier", 8, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)


# Get x,y coordinates for each state in the map
# def get_mouse_click_coor(x, y):
#     """Get x,y coordinates for each state in the map"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Get dataframe from csv file
df = pd.read_csv("50_states.csv")
state_names = df.state.to_list()
state_x_coor = df.x.to_list()
state_y_coor = df.y.to_list()

state_dict = {}

# Create a state_coor dict. key => state name, value => [x_cor, y_cor]
for i, state_name in enumerate(state_names):
    state_dict[state_name] = (state_x_coor[i], state_y_coor[i])

score = 0


def display_state(name):
    state_display = turtle.Turtle()
    state_display.hideturtle()
    state_display.penup()
    state_display.goto(state_dict[name])
    state_display.write(f"{name}", align="center", font=FONT)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while score < 50:
    if answer_state == "Exit":
        break
    if answer_state in state_dict:
        score += 1
        display_state(answer_state)
        del state_dict[answer_state]
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

# Write States to learn
df = pd.DataFrame(list(state_dict.keys()), columns=["US States to Learn"])
df.to_csv('States To Learn.csv')

