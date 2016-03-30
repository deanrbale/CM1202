#!/usr/bin/python3

from question import Question

class Test:
	'Class that is used to run a test'

	def __init__(self, moduleCode, numberOfQuestions = 20):
		self.__currentQuestion = 1
		self.__currentMark = 0
		self.__questions = [Question(moduleCode, i) for i in range(1, numberOfQuestions + 1)]

	def getQuestionDetails(self, questionNumber):
		return self.__questions[questionNumber - 1]

	def checkProvidedAnswer(self, questionNumber, ProvidedAnswer):

		return 

	def getCorrectAnswer(self, questionNumber):

		return

	def generateQuestion(self):

		return

	def questionPersonalistaion(self):

		return

	def markQuestion(self):

		return


	def saveMark(self):

		return

	def saveTotalMarks(self):


		return

	def exitTest(self):

		return