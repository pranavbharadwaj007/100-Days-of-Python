from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(question)


brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

print("You've completed the quiz.")
print(f"Final Score: {brain.score}/{brain.q_number}")