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
	labTitle = ttk.Label(popupMsg, text=message)
	labTitle.pack(side="top", pady=10)
	butOkay = ttk.Button(popupMsg, text="Okay", command = popupMsg.destroy)
	butOkay.pack()
	popupMsg.mainloop()

class MenuPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		column_0_xpad = 150
		row_0_ypad = 75

		self.lblTitle = tk.Label(self, text="Welcome to the Home Page", justify='center', font=EXTRA_LARGE_FONT, wraplength=300)
		self.lblTitle.grid( row=0, column=0,  columnspan=1,  rowspan=1, padx=(column_0_xpad,50), pady=(row_0_ypad,75), sticky="n")

		self.lblMessage = tk.Label(self, text="Welcome to group 4s Coursework application, I will fill this text in with a more helpful message at a later date", justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(column_0_xpad,50), pady=(0,50), sticky="w")

		self.lblInstructions = tk.Label(self, text="Select a module, then click to start the lesson or start the test", justify="left", font=NORMAL_FONT, wraplength=300)
		self.lblInstructions.grid(row=2, column=0, columnspan=1, rowspan=1, padx=(column_0_xpad,0), pady=(75,0), sticky="w")

		self.lblModule = tk.Label(self, text='Module:' , justify='left', font=NORMAL_FONT, wraplength=100)     
		self.lblModule.grid(row=1, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(0,0), sticky="ne")
		
		self.listModule = tk.Listbox(self, height= 5, width=50, font=SMALL_FONT, selectmode=tk.SINGLE) 
		self.scroll = ttk.Scrollbar(self, command= self.listModule.yview)                     
		self.listModule.configure(yscrollcommand=self.scroll.set)  

		for item in ["001", "002"]:                   
			self.listModule.insert(tk.END, item)  

		self.listModule.selection_set(0, tk.END)
		self.listModule.focus_set()

		self.listModule.grid(row=1, column=2, columnspan=1, rowspan=2, padx=(0,0), pady=(0,0), sticky="nw") 
		self.scroll.grid(row=1, column=3, columnspan=1,  rowspan=2, padx=(0,0), pady=(0,0), sticky="ne")  
		self.listModule.activate(0)

		self.butLesson = tk.Button(self, text="Lesson", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butLesson.bind("<Enter>", lambda event, x=self.butLesson: x.configure(bg="#80dfff"))
		self.butLesson.bind("<Leave>", lambda event, x=self.butLesson: x.configure(bg="#d9d9d9"))
		self.butLesson.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="w")   

		self.butTest = tk.Button(self, text="Test", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butTest.bind("<Enter>", lambda event, x=self.butTest: x.configure(bg="#80dfff"))
		self.butTest.bind("<Leave>", lambda event, x=self.butTest: x.configure(bg="#d9d9d9"))
		self.butTest.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="e")

class  TestPage(tk.Frame):

	def __init__(self, parent, controller, mCode, mName, lCompleted):
		tk.Frame.__init__(self, parent)
		self.__associatedModule = Module(mCode, mName, lCompleted)

		self.__moduleCode = mCode

		self.__column0xpad = 150
		self.__row0ypad = 75

		self.setIntructionPage()

		self.questionTemplate()
		self.hideQuestionTemplate()



	def setIntructionPage(self):

		self.labelVariable = tk.StringVar()
		self.labelVariable.set("You have selected to do the test for " + self.__moduleCode + " you only have one attempt. Please read the instructions thoroughly before you start the test.")

		self.lblTitle = tk.Label(self, text="Test Instructions", justify='center', font=EXTRA_LARGE_FONT, wraplength=300)
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

		self.lblQuestionNumber = tk.Label(self, text='', justify='left', font=EXTRA_LARGE_FONT, wraplength=300 )
		self.lblQuestionNumber.grid(row=0, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad, 50), pady=(self.__row0ypad,75), sticky='nw')

		self.lblQuestion = tk.Label(self, text='', justify='left', font=NORMAL_FONT, wraplength=600)
		self.lblQuestion.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(self.__column0xpad, 50), pady=(0,75), sticky='nw')

		self.butNext = tk.Button(self, text="Next", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butNext.bind("<Enter>", lambda event, x=self.butNext: x.configure(bg="#80dfff"))
		self.butNext.bind("<Leave>", lambda event, x=self.butNext: x.configure(bg="#d9d9d9"))
		self.butNext.grid(row=1, column=0, columnspan=2, rowspan=1, padx=(150,0), pady=(100,0), sticky="s")

	def displayQuestionDetails(self, question):

		self.lblQuestionNumber.configure(text='Question ' + str(question.getQuestionNumber()))
		self.lblQuestion.configure(text=str(question.getQuestionInfo()))



	def startTest (self):
		self.hideInstructions()

		startingQuestion = self.__associatedModule.getModuleTest().getQuestionDetails(1)

		self.displayQuestionDetails(startingQuestion)
		
		self.showQuestionTemplate()

	def showInstructions(self):

		self.lblTitle.grid()
		self.lblMessage.grid()
		self.butMenu.grid()
		self.butStart.grid()

	def showQuestionTemplate(self):

		self.lblQuestionNumber.grid()
		self.lblQuestion.grid()
		self.butNext.grid()


	def hideInstructions(self):

		self.lblTitle.grid_remove()
		self.lblMessage.grid_remove()
		self.butMenu.grid_remove()
		self.butStart.grid_remove()

	def hideQuestionTemplate(self):

		self.lblQuestionNumber.grid_remove()
		self.lblQuestion.grid_remove()
		self.butNext.grid_remove()





class QuestionPage(tk.Frame):

	def __init__(self, parent, controller, mCode):
		tk.Frame.__init__(self, parent)

		column_0_xpad = 150
		row_0_ypad = 75

		self.lblTitle = tk.Label(self, text='', justify='left', font=LARGE_FONT, wraplength=300 )
		self.lblTitle.grid(row=0, column=0, columnspan=1, rowspan=1, padx=(column_0_xpad, 50), pady=(row_0_ypad,75), sticky='n')

		self.lblQuestion = tk.Label(self, text='', justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblQuestion.grid(row=0, column=0, columnspan=1, rowspan=1, padx=(column_0_xpad, 50), pady=(row_0_ypad,75), sticky='n')

		self.butNext = tk.Button(self, text="Next", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9")
		self.butNext.bind("<Enter>", lambda event, x=self.butNext: x.configure(bg="#80dfff"))
		self.butNext.bind("<Leave>", lambda event, x=self.butNext: x.configure(bg="#d9d9d9"))
		self.butNext.grid(row=1, column=1, columnspan=1, rowspan=1, padx=(150,0), pady=(100,0), sticky="sw")





class  LessonStartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.lblTitle = ttk.Label(self, text="Lesson", font=LARGE_FONT)
		self.lblTitle.grid(row=0, column=0, columnspan=2, sticky="N")

		self.butMenu = tk.Button(self, text="Menu")
		self.butMenu.grid(row=10, column=10, columnspan=2, sticky="N")