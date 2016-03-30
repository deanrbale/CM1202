#!/usr/bin/python3

from tkinter import * 

class Coursework(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.grid()



def main():
	root = Tk() 
	root.title("Coursework") 
	app = Coursework(root) 
	root.mainloop() 
	return

if __name__ == "__main__":
    main()