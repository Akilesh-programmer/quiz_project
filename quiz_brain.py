# Creating a class called QuizBrain
class QuizBrain:
    # Initalizing few attributes for the class.
    def __init__(self, q_list):
        # Setting the question number to 0
        self.question_number = 0
        # Storing the list of objects which contains question and answers.
        self.question_list = q_list
        # Creating a variable to store the score.
        self.score = 0
    
    # Creating a new method called still_has_question to check if there are more questions left. Returning True and False.
    def still_has_questions(self):
        if self.question_number + 1 > len(self.question_list):
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
        self.user_answer = input(f"Q.{self.question_number}: {self.current_question.text}   (True or False):  ")
        # Calling the check_answer method and checking the answer.
        self.check_answer(self.user_answer, self.current_question.answer)
    # Creating the check_answer method to see whether the answer is correct and doing some steps according to it.
    def check_answer(self, input, answer):
        # If the answer is correct
        if input.lower() == answer.lower():
            print("You got it right!")
            # Getting the socre up by one.
            self.score += 1
             # Showing the score of the user.
            print(f"Your current score is: {self.score} / {self.question_number}")
        # If the answer is incorrect
        else:
            print("You got it wrong")
            # Showing the score of the user.
            print(f"Your current score is: {self.score} / {self.question_number}")
        # Showing the  user what was the correct answer.
        # Printing a new line to improve the user experience.
        print("\n")
