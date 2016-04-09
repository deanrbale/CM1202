#!/usr/bin/python3

from question import Question

class Test:
	'Class that is used to run a test'

	def __init__(self, moduleCode, numberOfQuestions = 20):
		self.__currentQuestion = 1
		self.__currentMark = 0
		self.__questions = [Question(moduleCode, i) for i in range(1, numberOfQuestions + 1)]

	def getQuestionDetails(self, questionNumber = -1):
		if questionNumber == -1:
			return self.__questions[self.__currentQuestion - 1]
		else:
			return self.__questions[questionNumber - 1]

	def getCurrentQuestionNumber(self):
		return self.__currentQuestion

	def incCurrentQuestion(self):
		self.__currentQuestion += 1

	def incCurrentMark(self):
		self.__currentMark += 1

	def generateQuestion(self):

		return

	def questionPersonalistaion(self):

		return

	def checkAnswer(self, providedAnswer, questionNumber = -1):
		if questionNumber == -1:
			question = self.__questions[self.__currentQuestion - 1]
		else:
			question = self.__questions[questionNumber - 1]

		if str(providedAnswer) == str(question.getCorrectAnswer()):
			return True
		else:
			return False

	def saveTotalMarks(self, fName, LName, mCode, filename='test_marks.csv'):

		with open(filename, 'w') as csvfile:
			fileWriter = csv.writer(csvfile, delimiter=',')
			fileWriter.writerow(LName,fName,mCode,self.__currentMark)

	def exitTest(self):

		return