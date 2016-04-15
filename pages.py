import random as rdm
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tm
from tkinter import scrolledtext
from module import *
import csv
import statistics as st

EXTRA_LARGE_FONT = ("MS", 22, "bold")
L_FONT = ("Verdana", 12)
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

	def __init__(self, parent, controller, user):
		'Initialise all widgets of the menu frame.'
		tk.Frame.__init__(self, parent)

		# self.__column0xpad = 150
		# self.__row0ypad = 75

		self.__column0xpad = 50
		self.__row0ypad = 40

		self.lblTitle = tk.Label(self, text="Welcome " + user[1] + ' ' + user[2] +  " to the Home Page", justify='center', font=EXTRA_LARGE_FONT, wraplength=400)
		self.lblTitle.grid( row=0, column=0,  columnspan=1,  rowspan=1, padx=(self.__column0xpad,50), pady=(self.__row0ypad,75), sticky="n")

		if user[0] == 'lecturer':
			messageText = 'From here you can view lessons that your students will see. You can also edit these too! Select the module on the right and use the buttons below. \n \n You can also view the feedback given by your students to help improve this application.'
		else:
			messageText = 'You may view lessons that have been provided by your lecturers. Once you have familiarised yourself with them proceed to take the test. \n \n To do this click on the module and then click on the Lesson or Test button.'
		self.lblMessage = tk.Label(self, text=messageText, justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,50), pady=(0,0), sticky="w")

		self.lblModule = tk.Label(self, text='Module:' , justify='left', font=NORMAL_FONT, wraplength=100)     
		self.lblModule.grid(row=1, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="ne")
		
		self.listModule = tk.Listbox(self, height= 6, width=50, font=SMALL_FONT, selectmode=tk.SINGLE) 
		self.scroll = ttk.Scrollbar(self, command= self.listModule.yview)                     
		self.listModule.configure(yscrollcommand=self.scroll.set)  

		for item in ["001 - Counting", "002 - Probability"]:                   
			self.listModule.insert(tk.END, item)  

		self.listModule.selection_set(0,0)
		self.listModule.focus_set()

		self.listModule.grid(row=1, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="nw") 
		self.scroll.grid(row=1, column=3, columnspan=1,  rowspan=1, padx=(0,0), pady=(0,0), sticky="ns")  
		self.listModule.activate(0)

		self.butLesson = tk.Button(self, text="View Lesson", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butLesson.bind("<Enter>", lambda event, x=self.butLesson: x.configure(bg="#80dfff"))
		self.butLesson.bind("<Leave>", lambda event, x=self.butLesson: x.configure(bg="#d9d9d9"))
		self.butLesson.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(75,0), sticky="w")   

		self.butTest = tk.Button(self, text="Test", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butTest.bind("<Enter>", lambda event, x=self.butTest: x.configure(bg="#80dfff"))
		self.butTest.bind("<Leave>", lambda event, x=self.butTest: x.configure(bg="#d9d9d9"))
		self.butTest.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(75,0), sticky="e")

		self.butEdit = tk.Button(self, text="Edit Lesson", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butEdit.bind("<Enter>", lambda event, x=self.butEdit: x.configure(bg="#80dfff"))
		self.butEdit.bind("<Leave>", lambda event, x=self.butEdit: x.configure(bg="#d9d9d9"))
		self.butEdit.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(75,0), sticky="e")

		self.butFeedback = tk.Button(self, text="View Feedback", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butFeedback.bind("<Enter>", lambda event, x=self.butFeedback: x.configure(bg="#80dfff"))
		self.butFeedback.bind("<Leave>", lambda event, x=self.butFeedback: x.configure(bg="#d9d9d9"))
		self.butFeedback.grid(row=2, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad + 130,0), pady=(75,0), sticky="w")

		self.hideAppropriateButtons(user)

	def hideAppropriateButtons(self, user):

		if user[0] == 'lecturer':
			self.butTest.grid_remove()
		else:
			self.butFeedback.grid_remove()
			self.butEdit.grid_remove()

class  TestFrame(tk.Frame):
	'Test frame'

	def __init__(self, parent, controller, mCode, mName, user, lCompleted):
		'Initialise all main widgets of the test frame.'
		tk.Frame.__init__(self, parent)
		self.__associatedModule = Module(mCode, mName, lCompleted)
		self.__user = user

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
		self.labelVariable.set("You have selected to do the test for " + self.__associatedModule.getModuleCode() + " you only have one attempt. Please read the instructions thoroughly before you start the test. \n \n You must answer all 20 questions of this test. Each question is multiple choice and you must decide between 4 answers. Once you have selected your answer you must then click on the next button. You will be given instant feedback on the question. After all 20 questions have been answered, you will be able to review the whole test.")

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

		self.lblFeedbackTitle = tk.Label(self, textvariable=self.varFeedbackTitle, justify='center', font=EXTRA_LARGE_FONT, wraplength=400)
		self.lblFeedbackTitle.grid( row=0, column=0,  columnspan=1,  rowspan=1, padx=(self.__column0xpad,50), pady=(self.__row0ypad,20), sticky="n")

		self.lblFeedbackMessage = tk.Label(self, textvariable=self.varFeedback, justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblFeedbackMessage.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,50), pady=(20,50), sticky="w")

		self.lblMarks = tk.Label(self, text='0/20', justify='left', font=EXTRA_LARGE_FONT)
		self.lblMarks.grid(row=0, column=2, columnspan=1, rowspan=1, padx=(400,0), pady=(self.__row0ypad,20), sticky="w")

		self.addListbox()

		self.addDetailsTemplate()

		self.butFeedbackMenu = tk.Button(self, text="Finished", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butFeedbackMenu.bind("<Enter>", lambda event, x=self.butFeedbackMenu: x.configure(bg="#80dfff"))
		self.butFeedbackMenu.bind("<Leave>", lambda event, x=self.butFeedbackMenu: x.configure(bg="#d9d9d9"))
		self.butFeedbackMenu.grid(row=6, column=2, columnspan=1, rowspan=1, padx=(300,0), pady=(75,0), sticky="w")

	def addDetailsTemplate(self):

		self.lblFeedbackQuestion = tk.Label(self, text='', justify='left', font=NORMAL_FONT, wraplength=500, height=5)
		self.lblFeedbackQuestion.grid(row=1, column=2, columnspan=2, rowspan=1, padx=(40,50), pady=(20,20), sticky="w")

		self.lblCorrectTitle = tk.Label(self, text='Correct Answer:', font=NORMAL_FONT, justify='left')
		self.lblCorrectTitle.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(25,0), sticky='w')

		self.lblCorrect = tk.Label(self, text='', font=NORMAL_FONT, justify='left')
		self.lblCorrect.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(0,0), sticky='w')

		self.lblGivenTitle = tk.Label(self, text='Selected Answer:', font=NORMAL_FONT, justify='left')
		self.lblGivenTitle.grid(row=4, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(25,0), sticky='w')

		self.lblGiven = tk.Label(self, text='', font=NORMAL_FONT, justify='left')
		self.lblGiven.grid(row=5, column=2, columnspan=1, rowspan=1, padx=(40,0), pady=(0,0), sticky='w')

	def addListbox(self ):

		self.listQuestions = tk.Listbox(self, height= 5, width=50, font=NORMAL_FONT, selectmode=tk.SINGLE)
		self.scroll = ttk.Scrollbar(self)

		self.listQuestions.configure(yscrollcommand=self.scroll.set)
		self.scroll.configure( command= self.listQuestions.yview)                     

		self.listQuestions.selection_set(0, tk.END)
		self.listQuestions.focus_set()

		self.listQuestions.grid(row=2, column=0, columnspan=1, rowspan=3, padx=(self.__column0xpad,0), pady=(25,0), sticky="nw") 
		self.scroll.grid(row=2, column=1, columnspan=1,  rowspan=3, padx=(0,0), pady=(25,0), sticky="ns") 

		self.listQuestions.bind("<<ListboxSelect>>", self.listQuestionClick)

		pass

	def listQuestionClick(self, event):

		selected = self.listQuestions.curselection()
		questionNumber = selected[0] + 1
		test = self.__associatedModule.getModuleTest()
		self.displayTestQuestionForFeedback(test, questionNumber)

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
		popupFeedback.geometry("500x400+500+200")
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
		butOkay.focus_set()

	def promptAnswer(self):
		'Method used to display question feedback.'

		popupFeedback = tk.Tk()
		popupFeedback.geometry("300x100+700+400")

		popupFeedback.wm_title("Attention!")
		labTitle = tk.Label(popupFeedback, text='You must select an answer\n before you can continue.', font=NORMAL_FONT)
		labTitle.pack(side="top", pady=10)
		butOkay = ttk.Button(popupFeedback, text="Okay", command = popupFeedback.destroy)
		butOkay.pack()

	def markQuestion(self, test, givenAnswer):
		'Mark the current question with the answer given and correct answer.'
		correct = test.checkAnswer(givenAnswer)
		if correct:
			test.incCurrentMark()
		question = test.getQuestionDetails()
		self.questionFeedback(question, givenAnswer, correct)	

	def displayTestQuestionForFeedback(self, test, questionNumber):
		question = test.getQuestionDetails(questionNumber)
		self.lblFeedbackQuestion.configure(text=question.getQuestionInfo())

		correct = question.getCorrectAnswer()
		selected = test.getSelectedAnswer(questionNumber)

		self.lblCorrect.configure(text=correct)
		self.lblGiven.configure(text=selected)

		if selected == correct:
			self.lblGiven.configure(fg='green')
		else:
			self.lblGiven.configure(fg='red')

	def colourListBox (self, test):

		for index in range(0, test.getNumberOfQuestions()):
			correct = test.getQuestionDetails(index + 1).getCorrectAnswer()
			selected = test.getSelectedAnswer(index + 1)

			if selected == correct:
				self.listQuestions.itemconfig(index, fg='green')
			else:
				self.listQuestions.itemconfig(index,fg='red')

	def displayTestData(self, test):

		if self.listQuestions.size() != 0:
			self.listQuestions.delete(0,self.listQuestions.size() -1 )
		testLength = test.getNumberOfQuestions()

		for item in range(1,testLength + 1):                   
			self.listQuestions.insert(tk.END, 'Question ' +str(item)  )

		self.lblMarks.configure(text=str(test.getCurrentMark()) + '/' + str(test.getNumberOfQuestions()))

		self.colourListBox(test)

		self.displayTestQuestionForFeedback(test, 1)
		self.listQuestions.activate(0)
		self.listQuestions.index(0)

	def nextQuestion(self):
		'Method used when going to the next question.'
		givenAnswer = self.__varAnswer.get()
		test = self.__associatedModule.getModuleTest()
		if givenAnswer == '':
			self.promptAnswer()
		else:
			self.markQuestion(test, givenAnswer)
			test.addSelectedAnswer(givenAnswer)
			if test.getCurrentQuestionNumber() == test.getNumberOfQuestions() :
				test.saveMarks(self.__user[1],self.__user[2])
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

	def setCommands(self, controller, menu):

		self.butMenu.configure(command=lambda: controller.show_frame(menu))
		self.butStart.configure(command=lambda: self.startTest())
		self.butFeedbackMenu.configure(command=lambda: controller.show_frame(menu))

class LectureFrame(tk.Frame):

	def __init__(self, parent , controller, moduleCode , user):
		tk.Frame.__init__(self, parent)
		self.__user = user
		self.__lesson = "lesson_"+ moduleCode+ ".txt"
		self.__title = 'title'
        #self.grid()
		self.draw_widgets()
		self.button()

    
	def draw_widgets(self):
	
		self.cframe = tk.Frame(self)
		self.cframe.grid(row=0, column=0, padx=(100,0), sticky='news')
		self.canv = tk.Canvas(self.cframe, width=976, height=540)  #612                    #this wraps text widgets within
		self.canv.grid(row=0, column=0, sticky='news')                       #a canvas so that they can be
		self.vscroll = tk.Scrollbar(self.cframe, orient=tk.VERTICAL, command=self.canv.yview) #scrolled through
		self.vscroll.grid(row=0, column=1, sticky='ns')
		self.canv["yscrollcommand"] = self.vscroll.set
		self.aframe = tk.Frame(self.canv)
		id = self.canv.create_window(0,0,window=self.aframe, anchor='nw')

		Num = 0
		file = open(self.__lesson,"r")
		for line in file:
			if line in ['\n', '\r\n']: #if line is blank move down a row
				self.w = tk.Label(self.fileInputFrame, text='', font=('Times', 15, 'bold'))
				self.w.grid(row=0, column=count)
				Num += 1			
			self.fileInputFrame = tk.Frame(self.aframe)
			self.fileInputFrame.grid(row = Num)
			count = 0
			wordLen = 0
			for word in line.split():
				wordLen = wordLen + len(word)
				if wordLen > 96:
					Num += 1
					self.fileInputFrame = tk.Frame(self.aframe) #is the length exceeds 110 move down a row
					self.fileInputFrame.grid(row = Num)	
					wordLen = 0				
				if word[0] == ".":
					if word[1] == "B":
						self.w = tk.Label(self.fileInputFrame, text = word[2:], font = ("Times", 15, "bold"))
						self.w.grid(row = 0, column = count)
						count += 1
					elif word[1] == "U":
						self.w = tk.Label(self.fileInputFrame, text = "\u2286", font = ("Times", 10, "bold"))
						self.w.grid(row = 0, column = count)
						count += 1
					elif word[1] == "I":
						self.w = tk.Label(self.fileInputFrame, text = word[2:], font = ("Times", 15, "italic"))
						self.w.grid(row = 0, column = count)
						count += 1
					elif word[1] == "F":
						if "/" in word:
							word = word[2:].split("/")
							if len(word[0]) > len(word[1]):
								Avg = len(word[0])
							else:
								Avg = len(word[1])  #gernerate an undeline length based on the longest of the 2
							underline = ""          #items in the fraction      
							for i in range(0,Avg+5):
								underline = underline + "-"					
							self.SubFrame = tk.Frame(self.fileInputFrame)
							self.SubFrame.grid(row = 0,column = count)
							self.w = tk.Label(self.SubFrame, text = word[0], font = ("Times", 12), anchor = 's')
							self.w.grid(row = 0, column = 0) #top of fraction
							self.w = tk.Label(self.SubFrame, text = underline, font = ("Times", 4))
							self.w.grid(row = 1, column = 0) #underline of fraction
							self.v = tk.Label(self.SubFrame, text = word[1], font = ("Times", 12), anchor = 'n')
							self.v.grid(row = 2, column = 0) #bottom of fraction
							count += 1
					elif word[1] == "S":
						if word[2] == "P":
							self.SubFrame = tk.Frame(self.fileInputFrame)
							self.SubFrame.grid(row = 0,column = count)
							self.w = tk.Label(self.SubFrame, text = word[3:], font = ("Times", 9))
							self.w.grid(row = 0, column = 0)
							self.v = tk.Label(self.SubFrame, text = "", font = ("Times", 6))
							self.v.grid(row = 1, column = 0) #superscript
							count += 1
						elif word[2] == "B":
							self.SubFrame = tk.Frame(self.fileInputFrame)
							self.SubFrame.grid(row = 0,column = count)
							self.w = tk.Label(self.SubFrame, text = word[3:], font = ("Times", 9))
							self.w.grid(row = 1, column = 0)
							self.v = tk.Label(self.SubFrame, text = "", font = ("Times", 6))
							self.v.grid(row = 0, column = 0) #subscript
							count += 1
					else:
						self.w = tk.Label(self.fileInputFrame, text = word, font = ("Times", 15))
						self.w.grid(row = 0, column = count)
						count += 1 #still print text if it starts with . and is not a command
				else:
					self.w = tk.Label(self.fileInputFrame, text = word, font = ("Times", 15))
					self.w.grid(row = 0, column = count)
					count += 1
			Num += 1
			self.aframe.update_idletasks()
			self.canv["scrollregion"]=self.canv.bbox(tk.ALL) #update scroll region
		
	def button(self):
		self.ButtonFrame = tk.Frame(self)
		self.ButtonFrame.grid(row = 3) 
		

		self.butBack = ttk.Button(self.ButtonFrame, text='Back')
		self.butBack.grid(row = 0,column = 0,  pady=(25,0), padx=(0,50))	
		
		self.butTest = ttk.Button(self.ButtonFrame, text='Test')
		self.butTest.grid(row = 0,column = 2, pady=(25,0) )

		if self.__user[0] == 'lecturer':
			self.butTest.grid_remove()

	def setCommands(self, controller, menu, test):

		self.butBack.configure(command=lambda: controller.show_frame(menu))
		self.butTest.configure(command=lambda: controller.show_frame(test))

class EditorFrame(tk.Frame):
	def __init__(self, parent , controller, moduleCode):
		tk.Frame.__init__(self, parent)
		self.__lesson = "lesson_"+ moduleCode+ ".txt"
		#root.protocol('WM_DELETE_WINDOW', self.exit) ,this will ask if you want to save when you press the red [X]
		self.textbox()
		self.menubar()
		
	def textbox(self):
		self.textPad = scrolledtext.ScrolledText(self, width = 115, height = 32)
		read = open(self.__lesson,"r")
		self.textPad.insert('1.0',read.read()) #creates a textbox with the contents of the file
		self.textPad.grid(column = 0, row = 1, padx=(75,0))

	def save(self):
		file = open(self.__lesson,"w")
		data = self.textPad.get('1.0', tk.END) #reads the lines and saves them to the text file
		file.write(data)
		file.close()

	def exit(self, controller, menu):
		if tm.askyesno("","Do you wish to save before quitting?"):
			self.save()
		controller.show_frame(menu)


	def help(self):
		label = tm.showinfo("Help", "Basic commands: .B - bold .I - italics .SB - subscript .SP - superscript .F - fraction .U - subset")

	def menubar(self):
		self.ButtonFrame = tk.Frame(self)
		self.ButtonFrame.grid(row = 0) 
		
		self.butSave = ttk.Button(self.ButtonFrame, text='Save')
		self.butSave['command'] = self.save
		self.butSave.grid(row = 0,column = 1, pady=(20,20), padx=(25,25))

		self.butHelp = ttk.Button(self.ButtonFrame, text='Help')
		self.butHelp['command'] = self.help
		self.butHelp.grid(row = 0,column = 0, pady=(20,20))	
		
		self.butBack = ttk.Button(self.ButtonFrame, text='Back')
		self.butBack.grid(row = 0,column = 2, pady=(20,20))
		
	def setCommands(self, controller, menu):
		self.butBack.configure(command=lambda: self.exit(controller, menu))

class SearchScoresFrame(tk.Frame):
    
	def __init__(self, parent , controller):
                     
		tk.Frame.__init__(self, parent)  

		self.__column0xpad = 50
		self.__row0ypad = 25

		self.lblTitle = tk.Label(self, text='Test Results', justify='center', font=EXTRA_LARGE_FONT, wraplength=400)
		self.lblTitle.grid( row=0, column=0,  columnspan=5,  rowspan=1, padx=(self.__column0xpad,0), pady=(self.__row0ypad,0), sticky="n")

		self.lblMessage = tk.Label(self, text="Select what you wish to search in and enter a search query below", justify='center',font = L_FONT)
		self.lblMessage.grid(row=1, column=0, columnspan=5,  rowspan=1, padx=(self.__column0xpad,0), pady=(20,0), sticky="nw")

		self.userEnt = tk.Entry(self, width=30 , font=L_FONT)
		self.userEnt.grid(row=2, column=0, columnspan=2,  rowspan=1, padx=(self.__column0xpad,0), pady=(20,0), sticky="n")

		self.btSearch = ttk.Button(self, text='Search', command=lambda: self.fillListBoxWithSearch(False)) 
		self.btSearch.grid(row=2, column=2, columnspan=1,  rowspan=1, padx=(0,0), pady=(20,0), sticky="nw")

		self.mbutton1 = ttk.Button(self,text= "Display All", command=lambda: self.fillListBoxWithSearch(True)) 
		self.mbutton1.grid(row=2, column=3, columnspan=1,  rowspan=1, padx=(0,0), pady=(20,0), sticky="nw")
		
		self.butMenu = tk.Button(self, text="Back to Menu", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butMenu.bind("<Enter>", lambda event, x=self.butMenu: x.configure(bg="#80dfff"))
		self.butMenu.bind("<Leave>", lambda event, x=self.butMenu: x.configure(bg="#d9d9d9"))
		self.butMenu.grid(row=6, column=5, columnspan=1, rowspan=1, padx=(20,0), pady=(0,0), sticky="sw")

                 
		self.addResultsTextBox()
		self.addListbox()
		self.addStatsLabels()
                              
	def addStatsLabels(self):
		self.lblMean = tk.Label(self, text="Mean: ", justify='center',font = L_FONT)
		self.lblMean.grid(row=1, column=5, columnspan=1,  rowspan=1, padx=(25,0), pady=(20,0), sticky="sw")

		self.lblMedian = tk.Label(self, text="Median: ", justify='center',font = L_FONT)
		self.lblMedian.grid(row=2, column=5, columnspan=1,  rowspan=1, padx=(25,0), pady=(20,0), sticky="sw") 

		self.lblstdDev = tk.Label(self, text="Standard deviation: ", justify='center',font = L_FONT)
		self.lblstdDev.grid(row=3, column=5, columnspan=1,  rowspan=1, padx=(25,0), pady=(20,0), sticky="sw") 

		self.lblHigh = tk.Label(self, text="Highest: ", justify='center',font = L_FONT)
		self.lblHigh.grid(row=4, column=5, columnspan=1,  rowspan=1, padx=(25,0), pady=(30,0), sticky="sw")

		self.lblLow = tk.Label(self, text="Lowest: ", justify='center',font = L_FONT)
		self.lblLow.grid(row=5, column=5, columnspan=1,  rowspan=1, padx=(25,0), pady=(20,0), sticky="nw")                                                  
                                  


	def addListbox(self):

		self.listSearchLabel = tk.Label(self, text='Select where you wish to search in' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.listSearchLabel.grid(row=3, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,0), pady=(20,20), sticky="sw")

		self.listSearch = tk.Listbox(self, height= 3, width=40, font=SMALL_FONT, selectmode=tk.SINGLE)
		self.scrollSearch = ttk.Scrollbar(self)

		self.listSearch.configure(yscrollcommand=self.scrollSearch.set)
		self.scrollSearch.configure( command= self.listSearch.yview)                     

		for search in ['Forename', 'Surname', 'Module']:
			self.listSearch.insert(tk.END, search)

		self.listSearch.selection_set(0,0)
		self.listSearch.focus_set()


		self.listSearch.grid(row=4, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,0), pady=(10,0), sticky="ne") 
		self.scrollSearch.grid(row=4, column=1, columnspan=1,  rowspan=1, padx=(0,0), pady=(10,0), sticky="nsw")

	def addResultsTextBox(self):


		self.txtbxResults = tk.Text (self, width=62, height=13 ,font=L_FONT, state=tk.DISABLED)
		self.scrollResults = ttk.Scrollbar(self)

		self.txtbxResults.configure(yscrollcommand=self.scrollResults.set)
		self.scrollResults.configure( command= self.txtbxResults.yview)

		self.txtbxResults.grid(row=5, column=0, columnspan=3,  rowspan=2, padx=(self.__column0xpad,0), pady=(20,0), sticky="ne")
		self.scrollResults.grid(row=5, column=3, columnspan=1,  rowspan=2, padx=(0,0), pady=(20,0), sticky="nsw")

	def fillListBoxWithSearch(self, displayAll):
		self.txtbxResults.configure(state=tk.NORMAL)
		self.txtbxResults.delete('0.0',tk.END)
		self.clearStats()

		selected = self.listSearch.curselection()
		if len(selected) == 1 or displayAll:

			if len(selected) == 1:
				if selected[0] == 0:
					section = 1
				elif selected[0] == 1:
					section = 0
				elif selected[0] == 2:
					section = 2

			userSearch = self.userEnt.get()
			markList = []
			with open('test_marks.csv') as csvfile:
				rdr = csv.reader(csvfile, delimiter=',')
				for row in rdr:
					try:
						if displayAll or (userSearch.lower() in row[section].lower()):
							formattedText = row[0] + ' - ' + row[1] + ' - ' + row[2] + ' - ' + row[3] + ' - ' + row[4] + ' - ' + row[5] + '\n'
							markList.append(int(row[3]))
							self.txtbxResults.insert(tk.END, str(formattedText))
					except:
						pass
			if len(markList) != 0:
				self.displayStats(markList)
		self.txtbxResults.configure(state=tk.DISABLED)

	def clearStats(self):

		self.lblMean.configure(text='Mean:')
		self.lblMedian.configure(text='Median:')
		self.lblstdDev.configure(text='Standard deviation:')
		self.lblHigh.configure(text='Highest:')
		self.lblLow.configure(text='Lowest:')

	def displayStats(self, markList):

		meanMark = st.mean(markList)
		medianMark = st.median(markList)
		stdevMark = st.stdev(markList)
		maxMark = max(markList)
		minMark = min(markList)


		self.lblMean.configure(text='Mean: {0:.2f}'.format(round(meanMark,2)))
		self.lblMedian.configure(text='Median: {0:.2f}'.format(round(medianMark,2)))
		self.lblstdDev.configure(text='Standard deviation: {0:.2f}'.format(round(stdevMark,2)))
		self.lblHigh.configure(text='Highest: {0:d}'.format(maxMark))
		self.lblLow.configure(text='Lowest: {0:d}'.format(minMark))


	def setCommands(self, controller, menu):

		self.butMenu.configure(command=lambda: controller.show_frame(menu))

                                                                                                                                                                                                    
class FeedbackSubmitFrame(tk.Frame):

	def __init__(self, parent, controller, moduleList):
		tk.Frame.__init__(self, parent)

		self.__column0xpad = 90
		self.__row0ypad = 50

		self.lblTitle = tk.Label(self, text='User Feedback', justify='center', font=EXTRA_LARGE_FONT, wraplength=400)
		self.lblTitle.grid( row=0, column=0,  columnspan=2,  rowspan=1, padx=(self.__column0xpad,50), pady=(self.__row0ypad,0), sticky="n")

		self.lblMessage = tk.Label(self, text='Your feeback on this application would be appreciated' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,50), pady=(50,20),sticky="sw")
  

		self.butMenu = tk.Button(self, text="Back to Menu", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butMenu.bind("<Enter>", lambda event, x=self.butMenu: x.configure(bg="#80dfff"))
		self.butMenu.bind("<Leave>", lambda event, x=self.butMenu: x.configure(bg="#d9d9d9"))
		self.butMenu.grid(row=8, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,50), pady=(30,0), sticky="s")

		self.butSubmit = tk.Button(self, text="Submit", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butSubmit.bind("<Enter>", lambda event, x=self.butSubmit: x.configure(bg="#80dfff"))
		self.butSubmit.bind("<Leave>", lambda event, x=self.butSubmit: x.configure(bg="#d9d9d9"))
		self.butSubmit.grid(row=8, column=1, columnspan=3, rowspan=1, padx=(200,0), pady=(30,0), sticky="s")
		self.butSubmit.configure(command=lambda: self.submitFeedback())

		self.addAnonymous()
		self.addNameOption()
		self.addListbox(moduleList)
		self.addFeedbackTextBox()

	def addAnonymous(self):
		self.ckbxAnonymousvar = tk.IntVar()
		self.ckbxAnonymous = tk.Checkbutton(self, text='Select this box if you wish to remain anonymous', justify='left', font=NORMAL_FONT, variable=self.ckbxAnonymousvar)
		self.ckbxAnonymous.grid(row=2, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,0), pady=(50,0), sticky="sw")
		self.ckbxAnonymous.configure(command=lambda:  self.checkboxClick())

	def checkboxClick(self):
		if self.ckbxAnonymousvar.get() == 1:
			self.entNumber.configure(state=tk.DISABLED)
			self.entName.configure(state=tk.DISABLED)
		else:
			self.entNumber.configure(state=tk.NORMAL)
			self.entName.configure(state=tk.NORMAL)

	def addNameOption(self):

		self.lblName = tk.Label(self, text="Name", justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblName.grid(row=3, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,20), pady=(20,0), sticky="e")

		self.entName = ttk.Entry(self, width=30)
		self.entName.grid(row=3, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(20,0), sticky="w")

		self.lblNumber = tk.Label(self, text="Student Number", justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblNumber.grid(row=4, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,20), pady=(10,0), sticky="e")

		self.entNumber = ttk.Entry(self, width=30)
		self.entNumber.grid(row=4, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(10,0), sticky="w")
	
	def addListbox(self, moduleList):

		self.listModulesLabel = tk.Label(self, text='Select module associated with your feedback or whether it is a general comment' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.listModulesLabel.grid(row=1, column=2, columnspan=2, rowspan=1, padx=(0,0), pady=(0,20), sticky="sw")

		self.listModules = tk.Listbox(self, height= 3, width=60, font=SMALL_FONT, selectmode=tk.SINGLE)
		self.scroll = ttk.Scrollbar(self)

		self.listModules.configure(yscrollcommand=self.scroll.set)
		self.scroll.configure( command= self.listModules.yview)                     

		self.listModules.selection_set(0, tk.END)
		self.listModules.focus_set()

		self.listModules.grid(row=2, column=2, columnspan=2, rowspan=1, padx=(0,0), pady=(20,0), sticky="nw") 
		self.scroll.grid(row=2, column=4, columnspan=1,  rowspan=1, padx=(0,0), pady=(20,0), sticky="ns") 

		for mod in moduleList:                   
			self.listModules.insert(tk.END, mod)
		self.listModules.insert(tk.END, 'General Comment')
		self.listModules.insert(tk.END, 'Software Bug')


	def addFeedbackTextBox(self):

		self.lblFeedback = tk.Label(self, text='Leave your comments in the box below' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblFeedback.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="sw")


		self.txtbxFeedback = tk.Text (self, width=60, height=6 ,font=SMALL_FONT)
		self.scrollFeedback = ttk.Scrollbar(self)

		self.txtbxFeedback.configure(yscrollcommand=self.scrollFeedback.set)
		self.scrollFeedback.configure( command= self.txtbxFeedback.yview)

		self.butClear = ttk.Button(self, text="Clear")
		self.butClear.grid(row=3, column=3, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="s")
		self.butClear.configure(command=lambda: self.txtbxFeedback.delete('0.0', tk.END))

		self.txtbxFeedback.grid(row=4, column=2, columnspan=2,  rowspan=2, padx=(0,0), pady=(20,0), sticky="nw")
		self.scrollFeedback.grid(row=4, column=4, columnspan=1,  rowspan=2, padx=(0,0), pady=(20,0), sticky="ns")

		self.emptybox = self.txtbxFeedback.get('0.0', tk.END)

	def checkEntriesAreFilled(self):
		completed = True
		if self.ckbxAnonymousvar.get() == 0:
			if (self.entNumber.get() == '') or (self.entName.get() == ''):
				completed = False


		selection = self.listModules.curselection()
		if (len(selection) == 0):
			completed = False


		charPresent = False
		for char in self.txtbxFeedback.get('0.0', tk.END):
			if char.isalnum():
				charPresent = True
		if completed:
			completed = charPresent

		return completed 
		
	def getFeedback(self):
		feedbackInfo = []
		if self.ckbxAnonymousvar.get() == 0:
			feedbackInfo.append(self.entNumber.get())
			feedbackInfo.append(self.entName.get())
		else:
			feedbackInfo.append('Anonymous')
			feedbackInfo.append('Anonymous')
		selection = self.listModules.curselection()
		feedbackInfo.append(self.listModules.get(selection[0]))
		text = self.txtbxFeedback.get('0.0', tk.END)
		withoutNewLineText = text.replace('\n','|')
		feedbackInfo.append(withoutNewLineText)

		return feedbackInfo

	def promptFeedback(self, title, msg):
		'Method used to display ask for feedback.'

		popupFeedback = tk.Tk()
		popupFeedback.geometry("300x100+600+300")

		popupFeedback.wm_title(title)
		labTitle = tk.Label(popupFeedback, text=msg, font=NORMAL_FONT)
		labTitle.pack(side="top", pady=10)
		butOkay = ttk.Button(popupFeedback, text="Okay", command = popupFeedback.destroy)
		butOkay.pack()

	def submitFeedback(self):
		if self.checkEntriesAreFilled():
			feedbackInfo = self.getFeedback()
			try:
				with open('appFeedback.csv', 'a') as csvfile:
					fileWriter = csv.writer(csvfile, delimiter='~')
					fileWriter.writerow(feedbackInfo)
					self.promptFeedback('Submitted', 'Thank you for you feedback!')
			except IOError:
				print('error')
			else:
				pass
		else:
			self.promptFeedback("Attention!",'You must complete the feedback \n form before clicking submit .')

	def setCommands(self, controller, menu):
		self.butMenu.configure(command=lambda: controller.show_frame(menu))

class FeedbackReviewFrame(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.__column0xpad = 90
		self.__row0ypad = 50

		self.__allFeedback = []

		self.lblTitle = tk.Label(self, text='User Feedback', justify='center', font=EXTRA_LARGE_FONT, wraplength=400)
		self.lblTitle.grid( row=0, column=0,  columnspan=2,  rowspan=1, padx=(self.__column0xpad,50), pady=(self.__row0ypad,0), sticky="n")

		self.lblMessage = tk.Label(self, text='Here you can look at student feedback about this application.' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,50), pady=(30,0),sticky="sw")
  
		self.lblName = tk.Label(self, text='Name:' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblName.grid(row=4, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,50), pady=(20,0),sticky="sw")

		self.lblNumber = tk.Label(self, text='Student Number:' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblNumber.grid(row=5, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,50), pady=(20,0),sticky="sw")

		self.lblReference = tk.Label(self, text='Brief Description:' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblReference.grid(row=6, column=0, columnspan=2, rowspan=1, padx=(self.__column0xpad,50), pady=(20,0),sticky="sw")

		self.addListbox()
		self.fillListBoxWithFeedback()

		self.addFeedbackTextBox()


		self.butMenu = tk.Button(self, text="Back to Menu", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butMenu.bind("<Enter>", lambda event, x=self.butMenu: x.configure(bg="#80dfff"))
		self.butMenu.bind("<Leave>", lambda event, x=self.butMenu: x.configure(bg="#d9d9d9"))
		self.butMenu.grid(row=8, column=0, columnspan=5, rowspan=1, padx=(self.__column0xpad,50), pady=(30,0), sticky="s")

	def addFeedbackTextBox(self):

		self.lblFeedback = tk.Label(self, text='Feedback:' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblFeedback.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(30,0), pady=(0,0), sticky="sw")


		self.txtbxFeedback = tk.Text (self, width=60, height=10 ,font=SMALL_FONT, state=tk.DISABLED)
		self.scrollFeedback = ttk.Scrollbar(self)

		self.txtbxFeedback.configure(yscrollcommand=self.scrollFeedback.set)
		self.scrollFeedback.configure( command= self.txtbxFeedback.yview)

		# self.butClear = ttk.Button(self, text="Clear")
		# self.butClear.grid(row=3, column=3, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="s")
		# self.butClear.configure(command=lambda: self.txtbxFeedback.delete('0.0', tk.END))

		self.txtbxFeedback.grid(row=3, column=2, columnspan=2,  rowspan=3, padx=(30,0), pady=(20,0), sticky="nw")
		self.scrollFeedback.grid(row=3, column=4, columnspan=1,  rowspan=3, padx=(0,0), pady=(20,0), sticky="ns")

		self.emptybox = self.txtbxFeedback.get('0.0', tk.END)

	def addListbox(self):

		self.listFeedbackLabel = tk.Label(self, text='Select feedback to look at' , justify='left', font=NORMAL_FONT, wraplength=400)
		self.listFeedbackLabel.grid(row=2, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,0), pady=(20,20), sticky="sw")

		self.listFeedback = tk.Listbox(self, height= 3, width=60, font=SMALL_FONT, selectmode=tk.SINGLE)
		self.scroll = ttk.Scrollbar(self)

		self.listFeedback.configure(yscrollcommand=self.scroll.set)
		self.scroll.configure( command= self.listFeedback.yview)                     

		self.listFeedback.selection_set(0, tk.END)
		self.listFeedback.focus_set()

		self.listFeedback.bind("<<ListboxSelect>>", self.listFeedbackClick)

		self.listFeedback.grid(row=3, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad,0), pady=(20,0), sticky="nw") 
		self.scroll.grid(row=3, column=1, columnspan=1,  rowspan=1, padx=(0,0), pady=(20,0), sticky="ns") 

	def fillListBoxWithFeedback(self):
		self.listFeedback.delete(0,tk.END)
		with open('appFeedback.csv') as csvfile:
			rdr = csv.reader(csvfile, delimiter='~')
			for row in rdr:
				try:
					self.listFeedback.insert(tk.END, row[2] + ' - ' +row[0])
					self.__allFeedback.append(row)
				except:
					pass

	def listFeedbackClick(self, event):

		selected = self.listFeedback.curselection()
		feedbackIndex = selected[0]
		feedback = self.__allFeedback[feedbackIndex]
		

		self.lblName.configure(text = 'Name: ' + feedback[1])
		self.lblNumber.configure(text = 'Student Number: ' + feedback[0])
		self.lblReference.configure(text = 'Brief Description: ' + feedback[2])
		feedbackText = feedback[3]
		formattedFeedbackText = feedbackText.replace('|','\n')
		self.txtbxFeedback.configure(state=tk.NORMAL)
		self.txtbxFeedback.delete('0.0', tk.END)
		self.txtbxFeedback.insert('0.0', formattedFeedbackText)
		self.txtbxFeedback.configure(state=tk.DISABLED)


	def setCommands(self, controller, menu):
		self.butMenu.configure(command=lambda: controller.show_frame(menu))



