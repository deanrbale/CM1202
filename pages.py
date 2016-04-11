import random as rdm
import tkinter as tk
from tkinter import ttk
from module import *

EXTRA_LARGE_FONT = ("MS", 22, "bold")
LARGE_BUTTON_FONT = ("MS", 14, "bold")
LARGE_FONT= ("MS", 14, "bold")
NORMAL_FONT= ("MS", 12)
SMALL_FONT= ("MS", 10)
POPUP_TITLE_FONT= ("MS", 8, "bold")
POPUP_MESSAGE_FONT= ("MS", 6)

def popupMessage(message):

	popupMsg = tk.Tk()
	popupMsg.geometry("250x100")

	popupMsg.wm_title("Attention!")
	labTitle = tk.Label(popupMsg, text=message)
	labTitle.pack(side="top", pady=10)
	butOkay = ttk.Button(popupMsg, text="Okay", command = popupMsg.destroy)
	butOkay.pack()
	popupMsg.mainloop()




class LoginFrame(tk.Frame):
	'Login Frame'

	def __init__(self, parent, controller):
		'Initialise all widget of the login frame'
		tk.Frame.__init__(self, parent)

		# self.__column0xpad = 150
		# self.__row0ypad = 75

		self.__column0xpad = 120
		self.__row0ypad = 40
		self.lblTitle = tk.Label(self, text="Welcome to Group 4's Applictaion", justify='center', font=EXTRA_LARGE_FONT, wraplength=300)
		self.lblTitle.grid( row=0, column=0,  columnspan=2,  rowspan=1, padx=(self.__column0xpad,0), pady=(self.__row0ypad,75), sticky="n")

		self.lblMessage = tk.Label(self, text="Please fill in the details to log in", justify='center', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,0), pady=(0,50), sticky="n")

		self.lblUsername = tk.Label(self, text="Username", justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblUsername.grid(row=2, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad-50,0), pady=(0,0), sticky="w")

		self.entUsername = ttk.Entry(self, width=30)
		self.entUsername.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="w")

		self.lblPassword = tk.Label(self, text="Password", justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblPassword.grid(row=3, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad-50,0), pady=(0,50), sticky="w")

		self.entPassword = ttk.Entry(self, width=30, show='*')
		self.entPassword.grid(row=3, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(0,50), sticky="w")

		self.butShow = ttk.Button(self, text='Show', command=lambda: self.showPassword())
		self.butShow.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(0,50), sticky="w")

		self.butLogin = tk.Button(self, text="Login", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butLogin.bind("<Enter>", lambda event, x=self.butLogin: x.configure(bg="#80dfff"))
		self.butLogin.bind("<Leave>", lambda event, x=self.butLogin: x.configure(bg="#d9d9d9"))
		self.butLogin.grid(row=4, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,0), pady=(0,0), sticky="n")

	def showPassword(self):
		self.entPassword.configure(show='')
		self.butShow.configure(text='Hide', command=lambda: self.hidePassword())

	def hidePassword(self):
		self.entPassword.configure( show='*')
		self.butShow.configure(text='Show', command=lambda: self.showPassword())

class MenuFrame(tk.Frame):
	'Menu Frame'

	def __init__(self, parent, controller):
		'Initialise all widgets of the menu frame.'
		tk.Frame.__init__(self, parent)

		# self.__column0xpad = 150
		# self.__row0ypad = 75

		self.__column0xpad = 50
		self.__row0ypad = 40

		self.lblTitle = tk.Label(self, text="Welcome to the Home Page", justify='center', font=EXTRA_LARGE_FONT, wraplength=300)
		self.lblTitle.grid( row=0, column=0,  columnspan=1,  rowspan=1, padx=(self.__column0xpad,50), pady=(self.__row0ypad,75), sticky="n")

		self.lblMessage = tk.Label(self, text="Welcome to group 4s Coursework application, I will fill this text in with a more helpful message at a later date", justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,50), pady=(0,50), sticky="w")

		self.lblInstructions = tk.Label(self, text="Select a module, then click to start the lesson or start the test", justify="left", font=NORMAL_FONT, wraplength=300)
		self.lblInstructions.grid(row=2, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,0), pady=(75,0), sticky="w")

		self.lblModule = tk.Label(self, text='Module:' , justify='left', font=NORMAL_FONT, wraplength=100)     
		self.lblModule.grid(row=1, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="ne")
		
		self.listModule = tk.Listbox(self, height= 5, width=50, font=SMALL_FONT, selectmode=tk.SINGLE) 
		self.scroll = ttk.Scrollbar(self, command= self.listModule.yview)                     
		self.listModule.configure(yscrollcommand=self.scroll.set)  

		for item in ["001 - Counting", "002 - Probability"]:                   
			self.listModule.insert(tk.END, item)  

		self.listModule.selection_set(0, tk.END)
		self.listModule.focus_set()

		self.listModule.grid(row=1, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="nw") 
		self.scroll.grid(row=1, column=3, columnspan=1,  rowspan=1, padx=(0,0), pady=(0,0), sticky="ns")  
		self.listModule.activate(0)

		self.butLesson = tk.Button(self, text="Lesson", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butLesson.bind("<Enter>", lambda event, x=self.butLesson: x.configure(bg="#80dfff"))
		self.butLesson.bind("<Leave>", lambda event, x=self.butLesson: x.configure(bg="#d9d9d9"))
		self.butLesson.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="w")   

		self.butTest = tk.Button(self, text="Test", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butTest.bind("<Enter>", lambda event, x=self.butTest: x.configure(bg="#80dfff"))
		self.butTest.bind("<Leave>", lambda event, x=self.butTest: x.configure(bg="#d9d9d9"))
		self.butTest.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="e")

class  TestFrame(tk.Frame):
	'Test frame'

	def __init__(self, parent, controller, mCode, mName, lCompleted):
		'Initialise all main widgets of the test frame.'
		tk.Frame.__init__(self, parent)
		self.__associatedModule = Module(mCode, mName, lCompleted)

		# self.__column0xpad = 150
		# self.__row0ypad = 75

		self.__column0xpad = 50
		self.__row0ypad = 40

		self.setIntructionPage()

		self.questionTemplate()
		self.hideQuestionTemplate()

		self.feedbacktemplate()
		self.hideFeedbackTemplate()

	def setIntructionPage(self):
		'Create widgets for the instruction for the test.'

		#styleEdit = ttk.Style()
		#styleEdit.configure('TButton', width=15, font=LARGE_BUTTON_FONT)

		self.titleVariable = tk.StringVar()
		self.titleVariable.set(self.__associatedModule.getModuleName() + " Test Instructions")

		self.labelVariable = tk.StringVar()
		self.labelVariable.set("You have selected to do the test for " + self.__associatedModule.getModuleCode() + " you only have one attempt. Please read the instructions thoroughly before you start the test.")

		self.lblTitle = tk.Label(self, textvariable=self.titleVariable, justify='center', font=EXTRA_LARGE_FONT, wraplength=400)
		self.lblTitle.grid( row=0, column=0,  columnspan=1,  rowspan=1, padx=(self.__column0xpad,50), pady=(self.__row0ypad,75), sticky="n")

		self.lblMessage = tk.Label(self, textvariable=self.labelVariable, justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,50), pady=(0,50), sticky="w")


		self.butMenu = tk.Button(self, text="Back to Menu", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butMenu.bind("<Enter>", lambda event, x=self.butMenu: x.configure(bg="#80dfff"))
		self.butMenu.bind("<Leave>", lambda event, x=self.butMenu: x.configure(bg="#d9d9d9"))
		self.butMenu.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="e")

		self.butStart = tk.Button(self, text="Start Test", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butStart.bind("<Enter>", lambda event, x=self.butStart: x.configure(bg="#80dfff"))
		self.butStart.bind("<Leave>", lambda event, x=self.butStart: x.configure(bg="#d9d9d9"))
		self.butStart.grid(row=2, column=3, columnspan=1, rowspan=1, padx=(150,0), pady=(100,0), sticky="w")

	def questionTemplate(self):
		'Creates widgets for the basic template for the test questions.'

		self.lblQuestionNumber = tk.Label(self, text='', justify='left', font=EXTRA_LARGE_FONT, wraplength=300 )
		self.lblQuestionNumber.grid(row=0, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad, 50), pady=(self.__row0ypad,10), sticky='nw')

		self.lblQuestion = tk.Label(self, text='', justify='left', font=NORMAL_FONT, wraplength=600, height=6, width=100)
		self.lblQuestion.grid(row=1, column=0, columnspan=3, rowspan=1, padx=(0,0), pady=(0,10), sticky='nw')

		self.lblAnswerSelect = tk.Label(self, text='Select Answer:', justify='left', font=LARGE_FONT, wraplength=200)
		self.lblAnswerSelect.grid(row=2, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad, 50), pady=(0,20), sticky='nw')

		self.butNext = tk.Button(self, text="Next", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butNext.bind("<Enter>", lambda event, x=self.butNext: x.configure(bg="#80dfff"))
		self.butNext.bind("<Leave>", lambda event, x=self.butNext: x.configure(bg="#d9d9d9"))
		self.butNext.grid(row=5, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="es")
		self.butNext.configure(command=lambda: self.nextQuestion())

		self.createRadioButtons()

	def createRadioButtons(self):
		'Creates the radio button widgets used to select answers.'

		styleEdit = ttk.Style()
		styleEdit.configure('TRadiobutton', font=NORMAL_FONT)

		self.__varAnswer = tk.StringVar()

		self.radbutAnswer1 = ttk.Radiobutton(self, text='1', variable=self.__varAnswer, value='1')
		self.radbutAnswer2 = ttk.Radiobutton(self, text='2', variable=self.__varAnswer, value='2')
		self.radbutAnswer3 = ttk.Radiobutton(self, text='3', variable=self.__varAnswer, value='3')
		self.radbutAnswer4 = ttk.Radiobutton(self, text='4', variable=self.__varAnswer, value='4')

		self.radbutAnswer1.grid(row=3, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,0), pady=(0,0), sticky="nw")
		self.radbutAnswer2.grid(row=4, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,0), pady=(15,0), sticky="nw")
		self.radbutAnswer3.grid(row=3, column=1, columnspan=1, rowspan=1, padx=(50,0), pady=(15,0), sticky="nw")
		self.radbutAnswer4.grid(row=4, column=1, columnspan=1, rowspan=1, padx=(50,0), pady=(15,0), sticky="nw")

	def feedbacktemplate(self):

		self.varFeedbackTitle = tk.StringVar()
		self.varFeedbackTitle.set(self.__associatedModule.getModuleName() + " Test Feedback")

		self.varFeedback = tk.StringVar()
		self.varFeedback.set("Thank you for completing the test for the module " + self.__associatedModule.getModuleCode() + ". Please review each question and look at the ones that you got wrong, if any.")

		self.lblFeedbackTitle = tk.Label(self, textvariable=self.titleVariable, justify='center', font=EXTRA_LARGE_FONT, wraplength=400)
		self.lblFeedbackTitle.grid( row=0, column=0,  columnspan=1,  rowspan=1, padx=(self.__column0xpad,50), pady=(self.__row0ypad,20), sticky="n")

		self.lblFeedbackMessage = tk.Label(self, textvariable=self.labelVariable, justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblFeedbackMessage.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,50), pady=(20,50), sticky="w")

		self.lblMarks = tk.Label(self, text='0/20', justify='left', font=EXTRA_LARGE_FONT)
		self.lblMarks.grid(row=0, column=3, columnspan=1, rowspan=1, padx=(50,self.__column0xpad), pady=(self.__row0ypad,20), sticky="e")

		self.addSpinbox()

		self.addDetailsTemplate()

		self.butFeedbackMenu = tk.Button(self, text="Back to Menu", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butFeedbackMenu.bind("<Enter>", lambda event, x=self.butMenu: x.configure(bg="#80dfff"))
		self.butFeedbackMenu.bind("<Leave>", lambda event, x=self.butMenu: x.configure(bg="#d9d9d9"))
		self.butFeedbackMenu.grid(row=6, column=0, columnspan=4, rowspan=1, padx=(0,0), pady=(75,0), sticky="s")

	def addDetailsTemplate(self):

		self.lblFeedbackQuestion = tk.Label(self, text='default value', justify='left', font=NORMAL_FONT, wraplength=500, height=5)
		self.lblFeedbackQuestion.grid(row=1, column=2, columnspan=2, rowspan=1, padx=(40,50), pady=(20,20), sticky="w")

		self.lblCorrectTitle = tk.Label(self, text='Correct Answer:', font=NORMAL_FONT, justify='left')
		self.lblCorrectTitle.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(25,0), sticky='w')

		self.lblCorrect = tk.Label(self, text='default value', font=NORMAL_FONT, justify='left')
		self.lblCorrect.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(0,0), sticky='w')

		self.lblGivenTitle = tk.Label(self, text='Selected Answer:', font=NORMAL_FONT, justify='left')
		self.lblGivenTitle.grid(row=4, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(25,0), sticky='w')

		self.lblGiven = tk.Label(self, text='default value', font=NORMAL_FONT, justify='left')
		self.lblGiven.grid(row=5, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(0,0), sticky='w')

	def addSpinbox(self ):

		self.listQuestions = tk.Listbox(self, height= 5, width=50, font=NORMAL_FONT, selectmode=tk.SINGLE)
		self.scroll = ttk.Scrollbar(self)

		for item in range(1,21):                   
			self.listQuestions.insert(tk.END, 'Question ' +str(item)  )

		self.listQuestions.configure(yscrollcommand=self.scroll.set)
		self.scroll.configure( command= self.listQuestions.yview)                     

		self.listQuestions.selection_set(0, tk.END)
		self.listQuestions.focus_set()

		self.listQuestions.grid(row=2, column=0, columnspan=1, rowspan=3, padx=(self.__column0xpad,0), pady=(25,0), sticky="nw") 
		self.scroll.grid(row=2, column=1, columnspan=1,  rowspan=3, padx=(0,0), pady=(25,0), sticky="ns") 

		pass

	def displayQuestionDetails(self, question):
		'Edits widgets of the created in questionTemplate() with the details of the question passes as an argument'

		self.lblQuestionNumber.configure(text='Question ' + str(question.getQuestionNumber()))
		self.lblQuestion.configure(text=str(question.getQuestionInfo()))

		answerList =[]
		answerList.append(question.getCorrectAnswer())
		for answer in question.getIncorrectAnswers():
			answerList.append(answer)

		self.__varAnswer.set('')

		answer = rdm.choice(answerList)
		self.radbutAnswer1.configure(text=answer, value=answer)
		answerList.remove(answer)

		answer = rdm.choice(answerList)
		self.radbutAnswer2.configure(text=answer, value=answer)
		answerList.remove(answer)

		answer = rdm.choice(answerList)
		self.radbutAnswer3.configure(text=answer, value=answer)
		answerList.remove(answer)

		answer = rdm.choice(answerList)
		self.radbutAnswer4.configure(text=answer, value=answer)
		answerList.remove(answer)

	def questionFeedback(self, question, givenAnswer, correct):
		'Method used to display question feedback.'

		popupFeedback = tk.Tk()
		popupFeedback.geometry("500x400+500+300")
		popupFeedback.grid()
		popupFeedback.wm_title("Instant feedback!")

		lblTitle = tk.Label(popupFeedback, text='Instant feedback', font=LARGE_FONT, justify='center')
		lblTitle.grid(row=0, column=0, columnspan=1, rowspan=1, padx=(25,0), pady=(25,0), sticky="n")

		lblQuestionTitle = tk.Label(popupFeedback, text='Question:', font=NORMAL_FONT, justify='left')
		lblQuestionTitle.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(25,0), pady=(25,0), sticky='w')

		lblQuestion = tk.Label(popupFeedback, text=question.getQuestionInfo(), font=NORMAL_FONT, justify='left', wraplength=450)
		lblQuestion.grid(row=2, column=0, columnspan=1, rowspan=1, padx=(25,0), pady=(0,0), sticky='w')

		lblCorrectTitle = tk.Label(popupFeedback, text='Correct Answer:', font=NORMAL_FONT, justify='left')
		lblCorrectTitle.grid(row=3, column=0, columnspan=1, rowspan=1, padx=(25,0), pady=(25,0), sticky='w')

		lblCorrect = tk.Label(popupFeedback, text=question.getCorrectAnswer(), font=NORMAL_FONT, justify='left')
		lblCorrect.grid(row=4, column=0, columnspan=1, rowspan=1, padx=(25,0), pady=(0,0), sticky='w')

		lblGivenTitle = tk.Label(popupFeedback, text='Selected Answer:', font=NORMAL_FONT, justify='left')
		lblGivenTitle.grid(row=5, column=0, columnspan=1, rowspan=1, padx=(25,0), pady=(25,0), sticky='w')

		lblGiven = tk.Label(popupFeedback, text=givenAnswer, font=NORMAL_FONT, justify='left')
		lblGiven.grid(row=6, column=0, columnspan=1, rowspan=1, padx=(25,0), pady=(0,0), sticky='w')

		if correct:
			lblGiven.configure(fg='green')
		else:
			lblGiven.configure(fg='red')

		butOkay = ttk.Button(popupFeedback, text="Okay", command = popupFeedback.destroy)
		butOkay.grid(row=7, column=0, columnspan=1, rowspan=1, padx=(0,0), pady=(25,0), sticky="s")

	def promptAnswer(self):
		'Method used to display question feedback.'

		popupFeedback = tk.Tk()
		popupFeedback.geometry("300x100+700+400")

		popupFeedback.wm_title("Attention!")
		labTitle = tk.Label(popupFeedback, text='You must select an answer\n before you can continue.', font=NORMAL_FONT)
		labTitle.pack(side="top", pady=10)
		butOkay = ttk.Button(popupFeedback, text="Okay", command = popupFeedback.destroy)
		butOkay.pack()

	def markQuestion(self, givenAnswer):
		'Mark the current question with the answer given and correct answer.'
		correct = self.__associatedModule.getModuleTest().checkAnswer(givenAnswer)
		if correct:
			self.__associatedModule.getModuleTest().incCurrentMark()
		question = self.__associatedModule.getModuleTest().getQuestionDetails()



		self.questionFeedback(question, givenAnswer, correct)	

	def displayTestData(self, test):

		testLength = test.getNumberOfQuestions()
		
		


		pass

	def nextQuestion(self):
		'Method used when going to the next question.'
		givenAnswer = self.__varAnswer.get()
		test = self.__associatedModule.getModuleTest()
		if givenAnswer == '':
			self.promptAnswer()
		else:
			self.markQuestion(givenAnswer)
			if test.getCurrentQuestionNumber() == 20 :
				test.saveMarks('ForenameTest','SurnameTest')
				self.hideQuestionTemplate()
				self.displayTestData(test)
				self.showFeedbackTemplate()
			else:
				test.incCurrentQuestion()
				nextQuestionDetails = test.getQuestionDetails()
				self.displayQuestionDetails(nextQuestionDetails)

	def startTest (self):
		'Method used to start the test.'
		self.hideInstructions()

		startingQuestion = self.__associatedModule.getModuleTest().getQuestionDetails()

		self.displayQuestionDetails(startingQuestion)
		
		self.showQuestionTemplate()

	def showInstructions(self):
		'Shows the instruction page widgets.'

		self.lblTitle.grid()
		self.lblMessage.grid()
		self.butMenu.grid()
		self.butStart.grid()

	def showQuestionTemplate(self):
		'Shows the question template widgets'

		self.lblQuestionNumber.grid()
		self.lblQuestion.grid()
		self.butNext.grid()
		self.lblAnswerSelect.grid()
		self.radbutAnswer1.grid()
		self.radbutAnswer2.grid()
		self.radbutAnswer3.grid()
		self.radbutAnswer4.grid()

	def showFeedbackTemplate(self):

		self.lblFeedbackTitle.grid()
		self.lblFeedbackMessage.grid()
		self.lblMarks.grid()
		self.butFeedbackMenu.grid()
		self.listQuestions.grid()
		self.scroll.grid()
		self.lblFeedbackQuestion.grid()
		self.lblCorrectTitle.grid()
		self.lblCorrect.grid()
		self.lblGivenTitle.grid()
		self.lblGiven.grid()

	def hideInstructions(self):
		'Hides the instruction page widgets'

		self.lblTitle.grid_remove()
		self.lblMessage.grid_remove()
		self.butMenu.grid_remove()
		self.butStart.grid_remove()

	def hideQuestionTemplate(self):
		'Hides the question template widgets'

		self.lblQuestionNumber.grid_remove()
		self.lblQuestion.grid_remove()
		self.butNext.grid_remove()
		self.lblAnswerSelect.grid_remove()
		self.radbutAnswer1.grid_remove()
		self.radbutAnswer2.grid_remove()
		self.radbutAnswer3.grid_remove()
		self.radbutAnswer4.grid_remove()

	def hideFeedbackTemplate(self):

		self.lblFeedbackTitle.grid_remove()
		self.lblFeedbackMessage.grid_remove()
		self.lblMarks.grid_remove()
		self.butFeedbackMenu.grid_remove()
		self.listQuestions.grid_remove()
		self.scroll.grid_remove()
		self.lblFeedbackQuestion.grid_remove()
		self.lblCorrectTitle.grid_remove()
		self.lblCorrect.grid_remove()
		self.lblGivenTitle.grid_remove()
		self.lblGiven.grid_remove()


class  LessonFrame(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.lblTitle = ttk.Label(self, text="Lesson", font=LARGE_FONT)
		self.lblTitle.grid(row=0, column=0, columnspan=2, sticky="N")

		self.butMenu = tk.Button(self, text="Menu")
		self.butMenu.grid(row=10, column=10, columnspan=2, sticky="N")