import turtle
import pandas as pd

INPUT_PROMPT = "What's another state name?"
SCREEN_TITLE = "U.S States Game"

# setting up the screen, giving it a background image
screen = turtle.Screen()
screen.title(SCREEN_TITLE)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
already_guessed = []

states_info_df = pd.read_csv("50_states.csv")


while score < 50:
    answered_state = screen.textinput(title=f"{score}/50 States Correct", prompt=INPUT_PROMPT)
    formatted_answered_state = answered_state.title()

    # the state should exist in the dataframe and should not have already been guessed
    if formatted_answered_state in states_info_df['state'].values and formatted_answered_state not in already_guessed:
        score += 1

        print("correct")
        # print(states_info_df['state'][formatted_answered_state])
        answer_row_x = states_info_df.loc[states_info_df['state'] == formatted_answered_state]['x'].item()
        answer_row_y = states_info_df.loc[states_info_df['state'] == formatted_answered_state]['y'].item()

        # new turtle writing at position of state
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(answer_row_x,answer_row_y)
        t.write(formatted_answered_state)

        already_guessed.append(formatted_answered_state)
    else:
        print("incorrect")


screen.exitonclick()




