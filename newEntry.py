from tkinter import *
import os


def createEntry():
	wsje = Tk()
	wsje.title("ACG - New Journal Entry")
	wsje.geometry("300x200")
	wsje.attributes("-fullscreen", False)
	def show():
		label.config(text=clicked.get())
	#Get pathway for files. If windows use \\. If mac use /
	cwd = os.getcwd()
	arr = os.listdir(cwd+"\\AccountData")
	
	#Frame
	frame = Frame(wsje, padx=0, pady=0)
	frame.pack(expand=True) 
	
	# datatype of menu text
	clicked = StringVar()
	  
	# initial menu text
	clicked.set("")
	  
	# Create Dropdown menu
	drop = OptionMenu(frame, clicked , *arr )
	drop.pack()
	  
	# Create button, it will change label text
	button = Button(frame,  text = "click Me" , command = show ).pack()

	def addAccountFrame():
		drop = OptionMenu(frame, clicked , *arr )
		drop.pack()
		NewEntry = Entry(frame, width=30)

	

	button = Button(frame,  text = "click Me" , command = addAccountFrame ).pack()
	# Create Label
	label = Label(frame, text = " " )
	label.pack()
	  
	# Execute tkinter
	wsje.mainloop()


createEntry()