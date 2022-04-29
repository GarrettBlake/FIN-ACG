from tkinter import *
import os


def createEntry():
	#Intiate Tkinter Instance
	wsje = Tk()
	wsje.title("ACG - New Journal Entry")
	wsje.geometry("700x200")
	wsje.attributes("-fullscreen", False)
	
	#Frames
	frame = Frame(wsje, padx=20, pady=20)
	frame.pack(expand=True)

	#Grab Account Data
	cwd = os.getcwd()
	arr = os.listdir(cwd+"\\AccountData")
	# datatype of menu text
	#clicked = StringVar()
	  
	# initial menu text
	#clicked.set("")
	#drop = OptionMenu(frame, clicked , *arr )
	#drop.pack()



	def addAccountFrame():
		clicked = StringVar()
		drop = OptionMenu(frame, clicked , *arr )
		drop.pack()
		entry1 = Entry(frame, width=30)
		Label( #Sub-Header
    		frame, 
    		text="Test", 
    		font=("Times", "16")
    		)
		label = Label(frame, text = " " )
		label.config(text=clicked.get())
		label.pack()
		print(label)

	
	button = Button(frame,  text = "Add Another Account" , command=lambda: [addAccountFrame()] ).pack()

	wsje.mainloop()

createEntry()