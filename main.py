from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []
for question in question_data:
    Q = question["question"]
    A = question["correct_answer"]
    new_question = Question(Q, A)
    Question_bank.append(new_question)
print(Question_bank)

Quiz = QuizBrain(Question_bank)

while Quiz.still_has_questions:
    Quiz.next_question()

"""
The QuizData will take from : https://opentdb.com/  
"""