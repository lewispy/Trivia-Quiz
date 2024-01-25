from tkinter import *
from tkinter import messagebox
from quizBrain import Quiz

BG_COLOR = "#050B2C"


class UserInterface:
	def __init__(self, quiz: Quiz):
		self.quiz = quiz
		self.UI = Tk()
		self.UI.config(
			bg=BG_COLOR,
			padx=20,
			pady=20
		)
		self.UI.title("Trivia game")
		self.score = Label(
			text="Score: ",
			font=("Arial", 10),
			bg=BG_COLOR,
			fg="white"
		)
		self.score.grid(row=0, column=1, pady=10)

		self.canvas = Canvas(width=634, height=303, highlightthickness=0)
		self.BG_IMAGE = PhotoImage(file="Trivia bg 3.png")
		self.canvas.create_image(317, 151, image=self.BG_IMAGE)
		self.qu_text = self.canvas.create_text(
			300, 151,
			width=500,
			text="Example trivia question",
			font=("Arial", 14, "italic"),
			fill="white"
		)
		self.canvas.grid(row=1, column=0, columnspan=2)

		false_image = PhotoImage(file="images/false.png")
		true_image = PhotoImage(file="images/true.png")
		self.false_button = Button(
			image=false_image,
			highlightthickness=0,
			bg=BG_COLOR,
			command=self.false_command
		)
		self.true_button = Button(
			image=true_image,
			highlightthickness=0,
			bg=BG_COLOR,
			command=self.true_command
		)
		self.false_button.grid(row=2, column=0)
		self.true_button.grid(row=2, column=1)

		self.edit_canvas_text(self.quiz.quiz_prompt(self.quiz.q_count))

		self.UI.mainloop()

	def edit_canvas_text(self, question_text):
		self.canvas.itemconfig(
			self.qu_text,
			text=question_text
		)

	def edit_label_text(self):
		self.score.config(
			text=f"Score: {self.quiz.u_scores}/{self.quiz.q_count}"
		)

	def check_remaining(self):
		self.edit_label_text()
		if self.quiz.q_count >= self.quiz.q_length:
			self.warning()
		else:
			self.edit_canvas_text(self.quiz.quiz_prompt(self.quiz.q_count))

	def true_command(self):
		self.quiz.true_command()
		self.check_remaining()

	def false_command(self):
		self.quiz.false_command()
		self.check_remaining()

	def warning(self):
		messagebox.showinfo(
			title="Quizz info",
			message=f"No more questions!\nFinal score is {self.quiz.u_scores}/{self.quiz.q_count}"
		)
		for button in [self.false_button, self.true_button]:
			button.config(state="disabled")
