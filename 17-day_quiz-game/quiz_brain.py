class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    # TODO 3. Checking if it's the end of the quiz
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    # TODO 1. Asking the question
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    # TODO 2. Checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


