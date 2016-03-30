#!/usr/bin/python3

from test import Test

class Module:
	'Class containing the functionality to start a lesson, a test and view its own statistic'


	def __init__(self, code, name, lessonCompleted):
		self.__moduleCode = code
		self.__moduleName = name
		self.__moduleTest = Test(self.__moduleCode)
		self.__lessonCompleted = False

	def lessonNowCompleted(self):
		self.__lessonCompleted = True
		return

	def getModuleCode(self):
		return self.__moduleCode

	def getModuleName(self):
		return self.__moduleName



