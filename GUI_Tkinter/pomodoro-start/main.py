from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✓'
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(item_canvas,text='00:00')
    title_label.config(text="Timer")
    check_label.config(text='')
    global rep
    rep = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def time_start():
    global rep
    rep += 1
    work_minute = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if rep % 8 == 0:
        count_down(long_break)
        title_label.config(text='LONG BREAK', fg= "pink")
    elif rep % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='SHORT BREAK', fg='green')
    else:
        count_down(work_minute)
        title_label.config(text='WORKING', fg='blue')
        check_label.config()

            

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_minute = math.floor(count/60)
    count_second = math.floor(count%60)
    if count_second < 10 :
        count_second = f'0{count_second}'
    canvas.itemconfig(item_canvas, text=f"{count_minute}:{count_second}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        time_start()
        marks = ""
        work_sessions = math.floor(rep/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=450, height=300)
window.title('Pomodoro')
window.config(padx=50, pady=50, bg=YELLOW)

#create label
title_label = Label(text='Timer', font=('Ariel', 35, 'bold'), background=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)


#Start Button
start_button = Button(text='Start', font=('Ariel', 20, 'bold'), background = YELLOW, fg='black', highlightthickness=0)
start_button.grid(column=0, row= 2)
start_button.config(command=time_start)

#Reset Button
restart_button = Button(text='Restart', font=('Ariel', 20, 'bold'), background = YELLOW, fg='black', highlightthickness=0)
restart_button.grid(column=2, row= 2)
restart_button.config(command=reset_timer)


#Image with canvas
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file='tomato.png')
canvas.create_image(120,100,image = photo_image) 
item_canvas = canvas.create_text(130,115,text='00:00', fill='white', font=(FONT_NAME, 30,'bold'))
canvas.grid(column=1, row=1)

#Check-mark
check_label = Label(font=('Ariel', 15,'bold'), background=YELLOW, fg=GREEN)
check_label.grid(column=1, row=2)


window.mainloop()