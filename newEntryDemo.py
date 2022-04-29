from tkinter import *
import os


def createEntry():
	#Intiate Tkinter Instance
	wsje = Tk()
	wsje.title("ACG - New Journal Entry")
	wsje.geometry("300x200")
	wsje.attributes("-fullscreen", False)
	
	#Frames
	frame = Frame(wsje, padx=20, pady=20)
	frame.pack(expand=True)

	#Grab Account Data
	cwd = os.getcwd()
	arr = os.listdir(cwd+"\\AccountData")
	# datatype of menu text
	clicked = StringVar()
	  
	# initial menu text
	clicked.set("")
	drop = OptionMenu(frame, clicked , *arr )
	drop.pack()
	wsje.mainloop()

createEntry()