import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATE")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')
all_state = data.state.to_list()
score = 0
guessed_state = []

while True:
    answer_states = screen.textinput(title='Guess the states', prompt=f"What is the state's name?? {score}/53").title()
    
    if answer_states == 'Exit':
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        missing_state = [state for state in all_state if state not in guessed_state]

        stored_missing_stated = pandas.DataFrame(missing_state)
        stored_missing_stated.to_csv('missing_states')
        break

    if answer_states in all_state:
        turl = turtle.Turtle()
        turl.hideturtle()
        turl.penup()
        state_data = data[data.state == answer_states]
        turl.goto(int(state_data.x), int(state_data.y))
        turl.write(answer_states)
        score += 1
        guessed_state.append(answer_states)

