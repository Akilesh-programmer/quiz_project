# Importing the required things from other files.
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Creating a empty list named question_bank to store the question object.
question_bank = []

# Creating a for loop to iterate through the question_data.
for thing in question_data:
    # Creating a new question object with the respective text and answer.
    new_question = Question(thing["text"], thing["answer"])
    # Appending the newly created question object to the question_bank list.
    question_bank.append(new_question)




quiz = QuizBrain(question_bank)
while QuizBrain.still_has_questions():
    quiz.next_question()
