#!/usr/bin/python3

from question import Question
import csv
import datetime

class Test:
	'Class that is used to run a test'

	def __init__(self, moduleCode, numberOfQuestions = 20):
		self.__moduleCode = moduleCode
		self.__currentQuestion = 1
		self.__currentMark = 0
		self.__questions = [Question(moduleCode, i) for i in range(1, numberOfQuestions + 1)]

	def getQuestionDetails(self, questionNumber = -1):
		if questionNumber == -1:
			return self.__questions[self.__currentQuestion - 1]
		else:
			return self.__questions[questionNumber - 1]

	def getNumberOfQuestions(self):
		return (len(self.__questions))

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

	def saveMarks(self, fName, LName, filename='test_marks.csv'):

		now = datetime.datetime.now()
		nowDate = now.strftime('%d-%m-%Y')
		nowTime = now.strftime('%H:%M:%S')

		try:
			with open(filename, 'a') as csvfile:
				fileWriter = csv.writer(csvfile, delimiter=',')
				fileWriter.writerow([LName,fName,self.__moduleCode,self.__currentMark,nowDate,nowTime])
		except IOError:
			print('error')
		else:
			return


	def exitTest(self):

		return