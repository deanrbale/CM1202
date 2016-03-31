#!/usr/bin/python3

from tkinter import * 
from module import Module

class Menu(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		#master.minsize(width= 1500, height= 750)
		#master.maxsize(width= 1500, height= 750)
		master.geometry("1200x750+30+30")
		master.configure(background='white')
		self.createWelcomeMessages(master)
		self.createModuleSelect(master)
		self.createLessonButton(master)
		self.createTestButton(master)
		self.createExitButton(master)
		self.__modules =  [Module('001', 'Test name', False)]

	def createWelcomeMessages(self, master):
		lblTitle = Label(master, text="Welcome to Group 4's Application", bg="white" , font=('MS', 20, 'bold'))
		lblTitle.place(x = 375, y = 50, width= 450, height=25)

		lblMessage = Label(master, text="Please select a module and then choose \nto complete the lesson or test.",bg="white" , font=('MS', 12, 'bold'))
		lblMessage.place(x = 375, y = 80, width= 450, height=50)


	def createModuleSelect(self, master): 
		lblModule = Label(master, text='Module:',bg="white" ,  font=('MS', 10,'bold'))     
		lblModule.place(x = 475, y = 200, width= 50, height=10)
		
		self.listModule = Listbox(master, height= 3) 
		scroll = Scrollbar(master, command= self.listModule.yview)                     
		self.listModule.configure(yscrollcommand=scroll.set)  

		self.listModule.place(x = 550, y = 195, width= 150, height=50) 
		scroll.place(x = 690, y = 195, width= 25, height=50)                                      
		for item in ["001", "002", ""]:                   
			self.listModule.insert(END, item)  

		self.listModule.selection_set(END)

	def initiateLesson(self, event):



		return


	def initiateTest(self, event):



		return

	def exitApp(self, event):
		
			#sys.exit(0)
		return


	def createLessonButton(self, master):

		butLesson = Button(master, text='Start Lesson',font=('MS', 12,'bold')) 
		butLesson.place(x = 400, y = 400, width= 150, height=50)
		butLesson.bind('<Button-1>', self.initiateLesson(self))

	def createTestButton(self, master):

		butTest = Button(master, text='Start test',font=('MS', 12,'bold')) 
		butTest.place(x = 650, y = 400, width= 150, height=50)
		butTest.bind('<Button-1>', self.initiateTest(self))

	def createExitButton(self, master):

		butTest = Button(master, text='Exit',font=('MS', 12,'bold')) 
		butTest.place(x = 525, y = 500, width= 150, height=50)
		butTest.bind('<Button-1>', self.exitApp(self))




def main():
	root = Tk() 
	root.title("Coursework") 
	app = Menu(root) 
	root.mainloop() 
	return

if __name__ == "__main__":
    main()