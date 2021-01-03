# My Solution to Day 17 - Quiz Project & Benefits of OOP from 100 days of Code by Dr. Angela Yu

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {new_quiz.score}/ {new_quiz.question_number}")
