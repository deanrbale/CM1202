#!/usr/bin/python3

import csv

class Question:
	'Contains all information for a given question'

	def __init__(self, moduleCode, questionNumber, generatedQuestion= False):
		self.__questionNumber = questionNumber
		self.__generatedQuestion = generatedQuestion
		if not generatedQuestion:
			with open('test_'+ moduleCode +'.csv') as csvfile:
				rdr = csv.reader(csvfile, delimiter=',')
				for row in rdr:
					if int(row[0]) == questionNumber:
						self.__questionInformation = row[1]
						self.__correctAnswer = row[2]
						self.__incorrectAnswers = [row[3],row[4],row[5]]
		else:
			with open('testGen_'+ moduleCode +'.csv') as csvfile:
				rdr = csv.reader(csvfile, delimiter=',')
				for row in rdr:
					if int(row[0]) == questionNumber:
						self.__questionInformation = row[1]
						self.__correctAnswer = row[2]
						self.__incorrectAnswers = [row[3],row[4],row[5]]
			

	def __str__(self):
		a = 'Question Number: ' + str(self.__questionNumber) + ' | Question Information: ' + self.__questionInformation +  ' | Correct Answer: ' + self.__correctAnswer + ' | Incorrect Answers: ' + self.__incorrectAnswers[0] + ', '+ self.__incorrectAnswers[1] + ', '+ self.__incorrectAnswers[2]
		return aS

	def getGeneratedQuestion(self):
		return self.__generatedQuestion

	def getQuestionNumber(self):
		return self.__questionNumber

	def getQuestionInfo(self):
		return self.__questionInformation
	
	def getCorrectAnswer(self):
		return self.__correctAnswer

	def getIncorrectAnswers(self):
		return self.__incorrectAnswers
	
