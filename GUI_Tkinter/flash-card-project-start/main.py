from os import remove, times
from tkinter import *
import pandas
import random
import time

from pandas.core.frame import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
new_list = []
try:
    data = pandas.read_csv('data/to_learn.csv')
    
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='rescord')
else:
    to_learn = data.to_dict(orient='rescord')
    

def next_card_X():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= 'French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    flip_timer = window.after(3000,flip_card)

def is_known_Y():
    try:
        to_learn.remove(current_card)
        new_data = DataFrame(to_learn)
        new_data.to_csv('data/to_learn.csv', index=False)
    except ValueError:
        next_card_X()

def flip_card():
    global current_card 
    canvas.itemconfig(card_title, text = 'English', fill='white')
    canvas.itemconfig(card_word, text = current_card['English'], fill ='white')
    canvas.itemconfig(card_background, image = photo_back)


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)


#Create image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
photo_front = PhotoImage(file='images/card_front.png')
photo_back = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400,286, image=photo_front)
card_title = canvas.create_text(400, 140, text='English', font=('Ariel', 45, 'italic'))
card_word = canvas.create_text(400, 280,text='history', font=('Ariel', 67, 'bold'))
canvas.grid(column=0,row=0, columnspan=2)

#Button
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, bg='White',highlightthickness=0, command=is_known_Y)
right_button.grid(column=0,row=1) 

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image,background='White',highlightthickness=0, command=next_card_X)
wrong_button.grid(column=1,row=1) 



window.mainloop()
