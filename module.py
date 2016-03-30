#!/usr/bin/python3

from test import Test

class Module:
	'Class containing the functionality to start a lesson, a test and view its own statistic'


	def __init__(self, code, name):
		self.__moduleCode = code
		self.__moduleName = name
		self.__moduleTest = Test(self.__moduleCode)

	def getModuleCode(self):
		return self.__moduleCode

	def getModuleName(self):
		return self.__moduleName



