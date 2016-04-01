#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

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

		for F in (MenuPage, TestInstructionPage, LessonStartPage ):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(MenuPage)


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
		frame.qf()
		frame.tkraise()

		#^^^ above creates two test pages

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

		self.listModule.grid(row=1, column=2, columnspan=1, rowspan=2, padx=(0,0), pady=(0,0), sticky="nw") 
		self.scroll.grid(row=1, column=3, columnspan=1,  rowspan=2, padx=(0,0), pady=(0,0), sticky="ne")  


		self.butLesson = tk.Button(self, text="Lesson", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9", command=lambda: controller.show_frame(LessonStartPage))
		self.butLesson.bind("<Enter>", lambda event, x=self.butLesson: x.configure(bg="#80dfff"))
		self.butLesson.bind("<Leave>", lambda event, x=self.butLesson: x.configure(bg="#d9d9d9"))
		self.butLesson.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="w")   

		self.butTest = tk.Button(self, text="Test", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9",  command=lambda: self.gotoTest(controller))
		self.butTest.bind("<Enter>", lambda event, x=self.butTest: x.configure(bg="#80dfff"))
		self.butTest.bind("<Leave>", lambda event, x=self.butTest: x.configure(bg="#d9d9d9"))
		self.butTest.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="e")

	def gotoTest(self,controller):

		#TestInstructionPage.lblMessage.configure(bg="black")
		controller.show_frame(TestInstructionPage)


	def qf(self):
		print("1")
		pass

class  TestInstructionPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.__moduleCode = "placeholder"

		column_0_xpad = 150
		row_0_ypad = 75

		self.labelVariable = tk.StringVar()
		self.labelVariable.set("You have selected to do the test for ")

		self.lblTitle = tk.Label(self, text="Test Instructions", justify='center', font=EXTRA_LARGE_FONT, wraplength=300)
		self.lblTitle.grid( row=0, column=0,  columnspan=1,  rowspan=1, padx=(column_0_xpad,50), pady=(row_0_ypad,75), sticky="n")

		self.lblMessage = tk.Label(self, textvariable=self.labelVariable, justify='left', font=NORMAL_FONT, wraplength=400)
		self.lblMessage.grid(row=1, column=0, columnspan=1, rowspan=1, padx=(column_0_xpad,50), pady=(0,50), sticky="w")


		self.butMenu = tk.Button(self, text="Back to Menu", font=LARGE_BUTTON_FONT, height= 2, width=15, relief=tk.GROOVE, bg="#d9d9d9",  command=lambda: controller.show_frame(MenuPage))
		self.butMenu.bind("<Enter>", lambda event, x=self.butMenu: x.configure(bg="#80dfff"))
		self.butMenu.bind("<Leave>", lambda event, x=self.butMenu: x.configure(bg="#d9d9d9"))
		self.butMenu.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(0,0), pady=(100,0), sticky="e")
		print (self.__moduleCode)

	def setModuleCode(self, code):

		self.__moduleCode = code
		#self.labelVariable.set("hello")
		#lblMessage.configure(text="hello")

	def qf(self):
		print("2")
		pass



class  LessonStartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.lblTitle = ttk.Label(self, text="Lesson", font=LARGE_FONT)
		self.lblTitle.grid(row=0, column=0, columnspan=2, sticky="N")

		self.butMenu = ttk.Button(self, text="Menu",  command=lambda: controller.show_frame(MenuPage))
		self.butMenu.grid(row=10, column=10, columnspan=2, sticky="N")



def main():
	app = CourseworkApp()
	app.geometry("1280x720+150+50")
	app.mainloop()

if __name__ == "__main__":
    main()





