class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        answer = input(f"Q.{self.question_number}: {question.text}. (True/False)?: ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You are wrong")
        print(f"The correct answer was {question_answer}")
        print(f"Your current score is {self.score}/{len(self.question_list)}")
        print("\n")
