#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("MS", 12, "bold")
NORMAL_FONT= ("MS", 8)
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


class CourseworkApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_title(self, "Group 4 DQS Coursework")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.createMenuBar(container)

		self.frames = {}

		for F in (StudentMenuPage, TestInstructionPage, LessonStartPage ):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StudentMenuPage)


	def createMenuBar(self, container):
		menubar = tk.Menu(container)
		basicMenu = tk.Menu(menubar, tearoff=0)
		basicMenu.add_command(label="Account settings", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_command(label="Test scores", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_command(label="Logout", command=lambda: popupMessage("Not supported yet"))
		basicMenu.add_separator()
		basicMenu.add_command(label="Exit", command=quit)
		menubar.add_cascade(label="Menu", menu=basicMenu)

		tk.Tk.config(self, menu=menubar)

	def show_frame (self, cont):

		frame = self.frames[cont]
		frame.tkraise()


class StudentMenuPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		labTitle = ttk.Label(self, text="Welcome to the Home Page", font=LARGE_FONT)
		labTitle.pack(pady=10, padx=10)

		butTest = ttk.Button(self, text="Test",  command=lambda: controller.show_frame(TestInstructionPage))
		butTest.pack()

		butLesson = ttk.Button(self, text="Lesson",  command=lambda: controller.show_frame(LessonStartPage))
		butLesson.pack()

class  TestInstructionPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		labTitle = ttk.Label(self, text="Test Instructions", font=LARGE_FONT)
		labTitle.pack(pady=10, padx=10)

		butMenu = ttk.Button(self, text="Menu",  command=lambda: controller.show_frame(StudentMenuPage))
		butMenu.pack()

class  LessonStartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		labTitle = ttk.Label(self, text="Lesson", font=LARGE_FONT)
		labTitle.pack(pady=10, padx=10)

		butMenu = ttk.Button(self, text="Menu",  command=lambda: controller.show_frame(StudentMenuPage))
		butMenu.pack()



def main():
	app = CourseworkApp()
	app.geometry("1280x720")
	app.mainloop()

if __name__ == "__main__":
    main()





