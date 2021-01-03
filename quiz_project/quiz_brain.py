# ask the questions
# check if answer is correct
# check if we're at end of quiz

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        return self.question_number <= len(self.questions_list)-1

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {question.text}. (True/False)? ").lower()
        self.check_answer(user_input, question.answer.lower())
        return user_input

    def check_answer(self, user_answer, actual_answer):
        if user_answer == actual_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect")
        print(f"Correct Answer is {actual_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()



