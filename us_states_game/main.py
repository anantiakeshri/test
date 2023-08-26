import turtle as t
import pandas as pd

# Create a screen
screen = t.Screen()
screen.title("U.S states game")

# Load the image as a shape
image = "./us_states_game/blank_states_img.gif"
screen.addshape(image)

# Create a Turtle and set its shape to the loaded image
t.shape(image)

# Importing CSV data from 50_states_csv
data = pd.read_csv("us_states_game/50_states.csv")
states_list = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    # Creating a pop up box for taking input
    check_state = screen.textinput(title= f"{len(guessed_states)}/50 states correct", prompt="What's another state name?").title()

    if check_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("us_states_game/states_to_learn.csv")
        break

    if check_state in states_list:
        guessed_states.append(check_state)
        tim = t.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == check_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(check_state)
    
