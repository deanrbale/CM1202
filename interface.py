#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)

class CourseworkApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_title(self, "Group 4 DQS Coursework")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StudentMenuPage, TestInstructionPage, ExtraPage ):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StudentMenuPage)

	def show_frame (self, cont):

		frame = self.frames[cont]
		frame.tkraise()


class StudentMenuPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="Welcome to the Menu Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		butTest = ttk.Button(self, text="Test",  command=lambda: controller.show_frame(TestInstructionPage))
		butTest.pack()

		butLesson = ttk.Button(self, text="Extra",  command=lambda: controller.show_frame(ExtraPage))
		butLesson.pack()

class  TestInstructionPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="Test Instructions", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		butMenu = ttk.Button(self, text="Menu",  command=lambda: controller.show_frame(StudentMenuPage))
		butMenu.pack()

class  ExtraPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="Extra Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		butMenu = ttk.Button(self, text="Menu",  command=lambda: controller.show_frame(StudentMenuPage))
		butMenu.pack()



def main():
	app = CourseworkApp()
	app.mainloop()

if __name__ == "__main__":
    main()





