from question import Question

class Test:
	'Class that is used to run a test'

	def __init__(self, moduleCode):
		self.__currentQuestion = 1
		self.__currentMark = 0
		self.__questions = [Question(moduleCode) for i in range(1, 21)]

		