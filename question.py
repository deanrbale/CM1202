import csv

class Question:
	'Contains all information for a given question'

	def __init__(self, moduleCode, questionNumber):
		self.__questionNumber = questionNumber
		with open('test_' + moduleCode + '.csv') as csvfile:
			rdr = csv.reader(csvfile)
			for row in rdr:
				if row[0] == questionNumber:
					self.__questionInformation = row[1]
					self.__correctAnswer = row[2]
					self.__incorrectAnswers = [row[3],row[4],row[5]]

		
		