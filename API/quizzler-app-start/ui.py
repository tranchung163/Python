from tkinter import *

from requests.models import LocationParseError

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,background=THEME_COLOR)
        self.create_score_label()
        self.creat_canvas()
        self.button()
        self.get_next_question()
        self.window.mainloop()

    def create_score_label(self):
        self.score_lable = Label(text='Score: 0', fg="white",background=THEME_COLOR, font=("Ariel", 18,'bold'))
        self.score_lable.grid(column=1,row=0)
    
    def creat_canvas(self):
        self.canvas =Canvas(width=400, height=350,bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            text="Some question text", 
            fill=THEME_COLOR, font=("Ariel", 24, "italic"),
            width=280
            )
        self.canvas.grid(column=0, row=1,columnspan=2, pady=50,padx=20)
        

    def button(self):
        self.true_image = PhotoImage(file ='images/true.png')
        self.true_button = Button(image=self.true_image,highlightthickness=0,command= self.check_answer_right)
        self.true_button.grid(column=0,row=2)

        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_image, highlightthickness=0,command=self.check_answer_wrong)
        self.false_button.grid(column=1,row=2)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score Board: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the questions")
            self.true_button.config(state='disable')
            self.false_button.config(state='disable')

    def check_answer_right(self):
        user_answer = 'True'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def check_answer_wrong(self):
        user_answer = 'False'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, answer_is_right):
        if answer_is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)





