#!/usr/bin/python3

from pages import *
import tkinter as tk


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

		for F in (HomePage, LessonModule001 ):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		frame = TestModule001(container, self, "001")
		self.frames[TestModule001] = frame
		frame.grid(row=0, column=0, sticky='nsew')

		frame = TestModule002(container, self, "002")
		self.frames[TestModule002] = frame
		frame.grid(row=0, column=0, sticky='nsew')



		self.show_frame(HomePage)


	def createMenuBar(self, container):
		menubar = tk.Menu(container)
		basicMenu = tk.Menu(menubar, tearoff=0)
		basicMenu.add_command(label="Home", command=lambda: self.show_frame(MenuPage))
		basicMenu.add_separator()
		basicMenu.add_command(label="Account settings", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_command(label="Test scores", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_command(label="Logout", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_separator()
		basicMenu.add_command(label="Exit", command=quit)
		infoMenu = tk.Menu(menubar,tearoff=0)
		infoMenu.add_command(label="Help", command=lambda: popupMessage("Not supported yet"))
		infoMenu.add_separator()
		infoMenu.add_command(label="About", command=lambda: popupMessage("Not supported yet"))
		menubar.add_cascade(label="Menu", menu=basicMenu)
		menubar.add_cascade(label="Help", menu=infoMenu)

		tk.Tk.config(self, menu=menubar)

	def show_frame (self, cont):

		frame = self.frames[cont]
		frame.tkraise()

		#^^^ above creates two test pages

class HomePage (MenuPage):

	def __init__(self, parent, controller):
		MenuPage.__init__(self, parent, controller)
		self.butTest.configure(command=lambda: self.showSelectedModuleTest(controller))
		self.butLesson.configure(command=lambda: controller.show_frame(LessonModule001))

	def showSelectedModuleTest(self, controller):

		selection = self.listModule.curselection()
		if (len(selection) == 1):
			if (selection[0] == 0):
				controller.show_frame(TestModule001)
			elif (selection[0] == 1):
				controller.show_frame(TestModule002) 


class LessonModule001 (LessonStartPage):

	def __init__(self, parent, controller):
		LessonStartPage.__init__(self, parent, controller)
		self.butMenu.configure(command=lambda: controller.show_frame(HomePage))


class TestModule001 (TestPage):

	def __init__(self, parent, controller, mCode):
		TestPage.__init__(self, parent, controller, mCode)
		self.butMenu.configure(command=lambda: controller.show_frame(HomePage))

class TestModule002 (TestPage):

	def __init__(self, parent, controller, mCode):
		TestPage.__init__(self, parent, controller, mCode)
		self.butMenu.configure(command=lambda: controller.show_frame(HomePage))

def main():
	app = CourseworkApp()
	app.geometry("1280x720+150+50")
	app.mainloop()

if __name__ == "__main__":
    main()





