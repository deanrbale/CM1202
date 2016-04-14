#!/usr/bin/python3

from pages import *
import tkinter as tk
import csv
import tkinter.messagebox as tm


class CourseworkApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_title(self, "Group 4 DQS Coursework")

		container = tk.Frame(self)
		container.grid()
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.createMenuBar(container)

		self.frames = {}

		for F in (LoginPage, HomePage, TestScores, SearchPage):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		frame = TestModule001(container, self, "001", 'Counting')
		self.frames[TestModule001] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = TestModule002(container, self, "002", 'Probability')
		self.frames[TestModule002] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = LessonModule001(container, self, "001")
		self.frames[LessonModule001] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = LessonModule002(container, self, "002")
		self.frames[LessonModule002] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = Editor001(container, self, "001")
		self.frames[Editor001] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = Editor002(container, self, "002")
		self.frames[Editor002] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = UserFeedback(container, self, ['Module - 001', 'Module - 002'])
		self.frames[UserFeedback] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = ReviewFeedback(container, self)
		self.frames[ReviewFeedback] = frame
		frame.grid(row=0, column=0, sticky='nsew')



		self.show_frame(LoginPage)

	def createMenuBar(self, container):
		menubar = tk.Menu(container)
		basicMenu = tk.Menu(menubar, tearoff=0)
		basicMenu.add_command(label="Home", command=lambda: self.show_frame(HomePage))
		basicMenu.add_separator()
		basicMenu.add_command(label="Account settings", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_command(label="Test scores", command=lambda:  self.show_frame(TestScores))
		basicMenu.add_command(label="Logout", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_separator()
		basicMenu.add_command(label="Exit", command=quit)
		infoMenu = tk.Menu(menubar,tearoff=0)
		infoMenu.add_command(label="Help", command=lambda: popupMessage("Not supported yet"))
		infoMenu.add_command(label="Feedback", command=lambda: self.show_frame(UserFeedback)) #New Line Here
		infoMenu.add_separator()
		infoMenu.add_command(label="About", command=lambda: popupMessage("Not supported yet"))
		menubar.add_cascade(label="Menu", menu=basicMenu)
		menubar.add_cascade(label="Help", menu=infoMenu)

		tk.Tk.config(self, menu=menubar)

	def show_frame (self, cont):

		if cont != LoginPage:					
			self.createMenuBar(tk.Frame(self))
		frame = self.frames[cont]
		frame.tkraise()

class HomePage (MenuFrame):

	def __init__(self, parent, controller):
		MenuFrame.__init__(self, parent, controller)
		self.butTest.configure(command=lambda: self.showSelectedModuleTest(controller))
		self.butLesson.configure(command=lambda: self.showSelectedModuleLesson(controller))
		self.butEdit.configure(command=lambda: self.showSelectedModuleEditor(controller))
		self.butFeedback.configure(command=lambda: controller.show_frame(ReviewFeedback))

	def showSelectedModuleEditor(self, controller):

		selection = self.listModule.curselection()
		if (len(selection) == 1):
			if (selection[0] == 0):
				controller.show_frame(Editor001)
			elif (selection[0] == 1):
				controller.show_frame(Editor002) 

	def showSelectedModuleTest(self, controller):

		selection = self.listModule.curselection()
		if (len(selection) == 1):
			if (selection[0] == 0):
				controller.show_frame(TestModule001)
			elif (selection[0] == 1):
				controller.show_frame(TestModule002) 

	def showSelectedModuleLesson(self, controller):

		selection = self.listModule.curselection()
		if (len(selection) == 1):
			if (selection[0] == 0):
				controller.show_frame(LessonModule001)
			elif (selection[0] == 1):
				controller.show_frame(LessonModule002)

class LessonModule001 (LectureFrame):

	def __init__(self, parent, controller, mCode):
		LectureFrame.__init__(self, parent, controller, mCode)
		self.setCommands(controller, HomePage, TestModule001)

class LessonModule002 (LectureFrame):

	def __init__(self, parent, controller, mCode):
		LectureFrame.__init__(self, parent, controller, mCode)
		self.setCommands(controller, HomePage, TestModule002)

class Editor001(EditorFrame):

	def __init__(self, parent, controller, mCode):
		EditorFrame.__init__(self, parent, controller, mCode)
		self.setCommands(controller, HomePage)

class Editor002(EditorFrame):

	def __init__(self, parent, controller, mCode):
		EditorFrame.__init__(self, parent, controller, mCode)
		self.setCommands(controller, HomePage)

class TestModule001 (TestFrame):

	def __init__(self, parent, controller, mCode, mName, lCompleted=False):
		TestFrame.__init__(self, parent, controller, mCode, mName, lCompleted)
		self.setCommands(controller, HomePage)

class TestModule002 (TestFrame):

	def __init__(self, parent, controller, mCode, mName, lCompleted=False):
		TestFrame.__init__(self, parent, controller, mCode, mName, lCompleted)
		self.setCommands(controller, HomePage)

class TestScores(TestScoresFrame):

	def __init__(self, parent, controller):
		TestScoresFrame.__init__(self, parent, controller)
		self.setCommands(controller, SearchPage)

class SearchPage(SearchScoresFrame):

	def __init__(self, parent, controller):
		SearchScoresFrame.__init__(self,parent, controller)

class UserFeedback (FeedbackSubmitFrame):

	def __init__(self, parent, controller, moduleList):
		FeedbackSubmitFrame.__init__(self, parent, controller, moduleList)
		self.setCommands(controller, HomePage)

class ReviewFeedback(FeedbackReviewFrame):

	def __init__(self, parent, controller):
		FeedbackReviewFrame.__init__(self, parent, controller)
		self.setCommands(controller, HomePage)

class LoginPage (LoginFrame):

	def __init__(self, parent, controller):
		LoginFrame.__init__(self, parent, controller)
		self.butLogin.configure(command=lambda: self.vallogin(controller))

	def vallogin(self, controller):
		username = self.entUsername.get()
		password = self.entPassword.get()
		currentaccount = ""
		users = {}
		checked1 = False
		checked2 = False

		with open("login.csv") as csvfile:
			rdr = csv.reader(csvfile)
			headers = next(rdr, None)
			for rows in rdr:
				users[rows[3]] = (rows[4], rows[1])
			if username == "":
 				tm.showerror("Login error", "A username must be entered")
 				checked1 = True
			if password == "":
				tm.showerror("Login error", "A password must be entered")
				checked2 = True
		for k, v in users.items():
			if username == k and password == v[0]:
				if v[1] == 'student': #This would allow a seperate page to load if the user is a student
					controller.geometry("1100x618+150+50")
					controller.show_frame(HomePage)
					break
					#StudentProfile.start()
				if v[1] == 'lecturer': #This would allow a seperate page to load if the user is a lecturer
					controller.geometry("1100x618+150+50")
					controller.show_frame(HomePage)
					break
					#LecturerProfile.start()
		if username != k and checked1 == False:
			tm.showerror("Login error", "Your username is incorrect")
		if password != v[0] and checked2 == False:
			tm.showerror("Login error", "Your password is incorrect")



def main():

	app = CourseworkApp()
	app.geometry("500x500+500+100")
	app.mainloop()

if __name__ == "__main__":
    main()





