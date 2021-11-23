# Creating a class called QuizBrain
class QuizBrain:
    # Initalizing few attributes for the class.
    def __init__(self, q_list):
        # Setting the question number to 0
        self.question_number = 0
        # Storing the list of objects which contains question and answers.
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number > 11:
            return False
        else:
            return True
    
    # Craeting a method for the QuizBrain.
    def next_question(self):
        # Getting hold of the current question.
        self.current_question = self.question_list[self.question_number]
        # Adding 1 to question_number so that it will be starting from 1 whilg going to the next line instead of 0.
        self.question_number += 1
        # Showing the question to the user and getting the True of False input from him.
        self.answer = input(f"Q.{self.question_number}: {self.current_question.text}   (True or False):  ")