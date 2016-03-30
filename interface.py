#!/usr/bin/python3

from tkinter import * 

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

	def createWelcomeMessages(self, master):
		lblTitle = Label(master, text="Welcome to Group 4's Application", font=('MS', 20, 'bold'))
		lblTitle.place(x = 375, y = 50, width= 450, height=25)

		lblMessage = Label(master, text="Please select a module and then choose \nto complete the lesson or test.", font=('MS', 12, 'bold'))
		lblMessage.place(x = 375, y = 80, width= 450, height=50)


	def createModuleSelect(self, master): 
		lblModule = Label(master, text='Module:', font=('MS', 10,'bold'))     
		lblModule.place(x = 475, y = 200, width= 50, height=10)
		
		self.listModule = Listbox(master, height= 3) 
		scroll = Scrollbar(master, command= self.listModule.yview)                     
		self.listModule.configure(yscrollcommand=scroll.set)  

		self.listModule.place(x = 550, y = 195, width= 150, height=50) 
		scroll.place(x = 690, y = 195, width= 25, height=50)                                      
		for item in ["001", "002", ""]:                   
			self.listModule.insert(END, item)  

		self.listModule.selection_set(END)

	def createLessonButton(self, master):

		butLesson = Button(master, text='Start Lesson',font=('MS', 12,'bold')) 
		butLesson['command']=self.initiateLesson      #Note: no () after the method 
		butLesson.place(x = 400, y = 400, width= 150, height=50)

	def createTestButton(self, master):

		butLesson = Button(master, text='Start test',font=('MS', 12,'bold')) 
		butLesson['command']=self.initiateTest     #Note: no () after the method 
		butLesson.place(x = 650, y = 400, width= 150, height=50)


	def initiateLesson(self):

		return


	def initiateTest(self):

		return


def main():
	root = Tk() 
	root.title("Coursework") 
	app = Menu(root) 
	root.mainloop() 
	return

if __name__ == "__main__":
    main()