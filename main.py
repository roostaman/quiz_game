from question_model import Question
from data import question_data, categories
from quiz_brain import QuizBrain


def get_questions_by_category(category):
    question_bank = []
    for q in question_data:
        if q["category"] == category:
            question = Question(text=q["question"], answer=q["correct_answer"])
            question_bank.append(question)
    return question_bank


category = input("""Choose a category of questions!
Type: '1' for Geography, '2' for General Knowledge, '3' for Entertainment: Film""")

question_bank: list = get_questions_by_category(categories[category])

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz! \nTotal score: {quiz.score}/{quiz.question_number}")
