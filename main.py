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



# Creating the quiz object.
quiz = QuizBrain(question_bank)

# Creating a while loop to keep on show questions if there are still more questions.
while quiz.still_has_questions():
    # Calling the next question method.
    quiz.next_question()

# Printing the final things in the quiz. 
print("You have completed the quiz.")
print(f"Your final score is: {quiz.score} / {quiz.question_number}.")