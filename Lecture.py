import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

class LecSelect(Frame):
    def __init__(self, root):
        root.title("Lecture Select")
        Frame.__init__(self, root)
        self.grid()
        w = Label(self, text = "Select a lecture:", font = ("Times", 15, "bold"))
        w.grid(row = 0, column = 0)
        self.buttons()

    def L1(self):
        root.lesson = "lesson1.txt" #this is carried throughout so you can tell which lecture 
        self.destroy()              #is being viewed
        frame = Lecture(root)
        frame.tkraise()

    def L2(self):
        root.lesson = "lesson2.txt"
        self.destroy()
        frame = Lecture(root)
        frame.tkraise()		
		
    def buttons(self):
        butEdit = Button(self, text='Lesson 1 - Counting',font=('Times', 15,'bold'), height = 10, width = 50)
        butEdit['command'] = self.L1
        butEdit.grid(row = 1,column = 0)

        butEdit = Button(self, text='Lesson 2 - Probability',font=('Times', 15,'bold'), height = 10, width = 50)
        butEdit['command'] = self.L2
        butEdit.grid(row = 2,column = 0)

class Lecture(Frame):
    def __init__(self, root):
        root.title("Lecture")
        Frame.__init__(self, root)
        self.grid()
        self.draw_widgets()
        self.button()
    
    def draw_widgets(self):
	
        cframe = Frame(self)
        cframe.grid(row=1, sticky=N+S+E+W)
        canv = Canvas(cframe, width=900, height=500)                     #this wraps text widgets within
        canv.grid(row=0, column=0, sticky=N+S+E+W)                       #a canvas so that they can be
        vscroll = Scrollbar(cframe, orient=VERTICAL, command=canv.yview) #scrolled through
        vscroll.grid(row=0, column=1, sticky=N+S)
        canv["yscrollcommand"] = vscroll.set
        aframe = Frame(canv)
        id = canv.create_window(0,0,window=aframe, anchor=N+W)

        Num = 0
        file = open(root.lesson,"r")
        for line in file:
            if line in ['\n', '\r\n']: #if line is blank move down a row
                Num += 1			
            fileInputFrame = Frame(aframe)
            fileInputFrame.grid(row = Num)
            count = 0
            wordLen = 0
            for word in line.split():
                wordLen = wordLen + len(word)
                if wordLen > 110:
                    Num += 1
                    fileInputFrame = Frame(aframe) #is the length exceeds 110 move down a row
                    fileInputFrame.grid(row = Num)					
                if word[0] == ".":
                    if word[1] == "B":
                        w = Label(fileInputFrame, text = word[2:], font = ("Times", 15, "bold"))
                        w.grid(row = 0, column = count)
                        count += 1
                    elif word[1] == "U":
                        w = Label(fileInputFrame, text = "\u2286", font = ("Times", 10, "bold"))
                        w.grid(row = 0, column = count)
                        count += 1
                    elif word[1] == "I":
                        w = Label(fileInputFrame, text = word[2:], font = ("Times", 15, "italic"))
                        w.grid(row = 0, column = count)
                        count += 1
                    elif word[1] == "F":
                        word = word[2:].split("/")
                        if len(word[0]) > len(word[1]):
                            Avg = len(word[0])
                        else:
                            Avg = len(word[1])  #gernerate an undeline length based on the longest of the 2
                        underline = ""          #items in the fraction      
                        for i in range(0,Avg+5):
                             underline = underline + "-"					
                        SubFrame = Frame(fileInputFrame)
                        SubFrame.grid(row = 0,column = count)
                        w = Label(SubFrame, text = word[0], font = ("Times", 12), anchor = S)
                        w.grid(row = 0, column = 0) #top of fraction
                        w = Label(SubFrame, text = underline, font = ("Times", 4))
                        w.grid(row = 1, column = 0) #underline of fraction
                        v = Label(SubFrame, text = word[1], font = ("Times", 12), anchor = N)
                        v.grid(row = 2, column = 0) #bottom of fraction
                        count += 1
                    elif word[1] == "S":
                        if word[2] == "P":
                            SubFrame = Frame(fileInputFrame)
                            SubFrame.grid(row = 0,column = count)
                            w = Label(SubFrame, text = word[3:], font = ("Times", 9))
                            w.grid(row = 0, column = 0)
                            v = Label(SubFrame, text = "", font = ("Times", 6))
                            v.grid(row = 1, column = 0) #superscript
                            count += 1
                        elif word[2] == "B":
                            SubFrame = Frame(fileInputFrame)
                            SubFrame.grid(row = 0,column = count)
                            w = Label(SubFrame, text = word[3:], font = ("Times", 9))
                            w.grid(row = 1, column = 0)
                            v = Label(SubFrame, text = "", font = ("Times", 6))
                            v.grid(row = 0, column = 0) #subscript
                            count += 1
                    else:
                        w = Label(fileInputFrame, text = word, font = ("Times", 15))
                        w.grid(row = 0, column = count)
                        count += 1 #still print text if it starts with . and is not a command
                else:
                    w = Label(fileInputFrame, text = word, font = ("Times", 15))
                    w.grid(row = 0, column = count)
                    count += 1
            Num += 1
            aframe.update_idletasks()
            canv["scrollregion"]=canv.bbox(ALL) #update scroll region
			
    def Edit(self): 
        self.destroy()
        frame = Editor(root)
        frame.lift()

    def Test(self): 
        #needs to move to test
        self.destroy()
        frame = Test(root)
        frame.lift()       

    def Back(self): 
        self.destroy()
        frame = LecSelect(root)
        frame.lift()
		
    def button(self):
        ButtonFrame = Frame(self)
        ButtonFrame.grid(row = 16) 
		
        butEdit = Button(ButtonFrame, text='Edit',font=('Times', 15,'bold'))
        butEdit['command'] = self.Edit
        butEdit.grid(row = 0,column = 1)

        butEdit = Button(ButtonFrame, text='Back',font=('Times', 15,'bold'))
        butEdit['command'] = self.Back
        butEdit.grid(row = 0,column = 0)	
		
        butEdit = Button(ButtonFrame, text='Test',font=('Times', 15,'bold'))
        butEdit['command'] = self.Test
        butEdit.grid(row = 0,column = 2)

class Editor(Frame):
    def __init__(self, root):
        root.title("Text Editor")
        Frame.__init__(self, root)
        #root.protocol('WM_DELETE_WINDOW', self.exit) ,this will ask if you want to save when
        self.grid()                      # you press the red [X]
        self.textbox()
        self.menubar()
		
    def textbox(self):
        self.textPad = scrolledtext.ScrolledText(self, width = 115, height = 40)
        read = open(root.lesson,"r")
        self.textPad.insert('1.0',read.read()) #creates a textbox with the contents of the file
        self.textPad.grid(column = 0, row = 1)

    def save(self):
        file = open(root.lesson,"w")
        data = self.textPad.get('1.0', END) #reads the lines and saves them to the text file
        file.write(data)
        file.close()

    def exit(self):
        if messagebox.askyesno("","Do you wish to save before quitting?"):
            self.save()
            self.move()
        else:
            self.save()
            self.move()

    def move(self):
        self.destroy()
        frame = Lecture(root)
        frame.lift()

    def help(self):
        label = tkinter.messagebox.showinfo("Help", "Basic commands: .B - bold .I - italics .SB - subscript .SP - superscript .F - fraction .U - subset")

    def menubar(self):
        ButtonFrame = Frame(self)
        ButtonFrame.grid(row = 0) 
		
        butEdit = Button(ButtonFrame, text='Save',font=('Times', 15,'bold'))
        butEdit['command'] = self.save
        butEdit.grid(row = 0,column = 1)

        butEdit = Button(ButtonFrame, text='Help',font=('Times', 15,'bold'))
        butEdit['command'] = self.help
        butEdit.grid(row = 0,column = 0)	
		
        butEdit = Button(ButtonFrame, text='Back',font=('Times', 15,'bold'))
        butEdit['command'] = self.exit
        butEdit.grid(row = 0,column = 2)
		
root = Tk()
app = LecSelect(root)
root.mainloop()