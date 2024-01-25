from question import Question
from data import Data


class Quiz:

    def __init__(self):
        self.data = Data().get_data()
        Question.instant(self.data)
        self.questions = Question.all_questions
        self.q_length = len(self.questions)
        self.q_count = 0
        self.u_scores = 0
        self.answer = None

    def quiz_prompt(self, i):
        print(f"Q{i+1}: {self.questions[i].text}")
        print(f"{self.u_scores}/{self.q_count}")
        question = self.questions[i].text
        return question

    def true_command(self):
        self.answer = "True"
        self.__check_answer(i=self.q_count)
        self.q_count += 1

    def false_command(self):
        self.answer = "False"
        self.__check_answer(i=self.q_count)
        self.q_count += 1

    def __check_answer(self, i):
        print(f"User answer: {self.answer}")
        print(f"Answer: {self.questions[i].answer}")
        if self.answer == self.questions[i].answer:
            self.u_scores += 1
        else:
            pass
