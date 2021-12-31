class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0
    
    def still_has_question(self):
        lenList = len(self.question_list)
        current_number_question = self.question_number + 1
        if current_number_question > lenList:
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choose = input(f"Q.{self.question_number}: {current_question.text}? (True or False): ")
        self.check_answer(choose, current_question.answer)

    def check_answer(self, choose, answer):
        if choose.lower() == answer.lower():
            self.score += 1
            print(f"its True!! your score is {self.score}")
        else:
            print(f"its False!! your score is {self.score}")


    