# Creating a class called Question.
class Question:
    # Creating the initialize code for the Question class with text and answers as parametes.
    def __init__(self, q_text, q_answer):
        # Creating a text attribute with the help of input.
        self.text = q_text
        # Creating a answer attribute with the help of input.
        self.answer = q_answer

# Calling the Question class and passing the positional arguements.
new_q = Question("2 + 3 = 5", "True")

