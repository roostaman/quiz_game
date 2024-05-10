class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer == user_answer:
            print("You got it right! ")
            self.score += 1
        else:
            print("That's wrong. ")
        print(f"The correct answer is: {correct_answer}. "
              f"\nYour current score is: {self.score}/{self.question_number}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.check_answer(user_answer=answer, correct_answer=current_question.answer)
