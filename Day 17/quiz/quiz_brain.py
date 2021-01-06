class QuizBrain:

    def __init__(self, question_list):

        self.q_number = 0
        self.score = 0
        self.q_list = question_list


    def next_question(self):

        question = self.q_list[self.q_number]
        self.q_number += 1
        print()
        ans = input(f"Q.{self.q_number}: {question.text} (True/False)?: ")
        self.check_answer(ans, question.answer)


    def still_has_questions(self):

        if self.q_number < len(self.q_list):

            return True

        else:

            return False


    def check_answer(self, usr_ans, correct_ans):

        if usr_ans.lower() == correct_ans.lower():

            print("You got it right!")
            self.score += 1

        else:

            print("That's wrong.")

        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.q_number}.\n")