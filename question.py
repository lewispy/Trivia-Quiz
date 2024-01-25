import pandas as pd


class Question:
    all_questions = []  # An empty list to hold all instances of the Question class

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

        Question.all_questions.append(self)
    
    # A class method to instantiate question objects from data file
    @classmethod
    def instant(cls, data):  # Takes a list of dictionaries as argument for instantiation
        for question in data:
            t = question["question"]
            a = question["correct_answer"]
            if any(q.text == t for q in Question.all_questions):  # Checks to see if the question had already been instantiated
                continue
            else:
                Question(
                    text=t,
                    answer=a
                )  # If not, then instantiate
        print("Questions have been instantiated.")
    
    # A class method to convert question and answers to data frame (for expo purposes 😉.)
    @classmethod
    def convert_data(cls):
        question_list = []
        for question_object in Question.all_questions:
            question_list.append(question_object.__dict__)  # The dict keywords shows the attributes of each object in dictionary form

        df = pd.DataFrame(question_list).rename(columns=({"text":"Question", "answer": "Answer"}))
        return df
    
    # A magic method to customize the object appearances when printed    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.text}', '{self.answer}')"
