import requests
import html


class Data:
	def __init__(self):
		try:
			self.response = requests.get(
				url="https://opentdb.com/api.php",
				params={"amount": 50, "type": "boolean"}
			)
			self.response.raise_for_status()
		except requests.exceptions.RequestException as e:
			print(f"There is an error!\n{e}")

	def get_data(self):
		questions = self.response.json()["results"]
		for question in questions:
			question["question"] = html.unescape(question["question"])
		return questions
