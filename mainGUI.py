from tkinter import *
from tkinter import messagebox
from accountCreator import createAccount
from newEntry import createEntry
import os
import pandas as pd


#Establish Window
ws = Tk()
ws.title('ACG Main')
ws.geometry('1920x1080')
ws.config(bg="#447c84")
ws.attributes('-fullscreen', True)



#Get Current Accounts
cwd = os.getcwd()
arr = os.listdir(cwd+"\\AccountData")
df = pd.DataFrame(data=arr, columns=[''])


#Upon Button Click
def newAccount():
    createAccount()
def newEntry():
    createEntry()
def refreshButton():
    cwd = os.getcwd()
    arr = os.listdir(cwd+"\\AccountData")
    df = pd.DataFrame(data=arr, columns=[''])
    return df


#Frames
frame = Frame(ws, padx=20, pady=20)
frame.pack(expand=True)
Label( #Title
    frame, 
    text='Financial Accounting Dashboard', 
    font=("Times", "24", "bold")
    ).grid(row=0, columnspan=1, pady=10)

Label( #Header
    frame, 
    text='Current Accounts', 
    font=("Times", "18", "bold")
    ).grid(row=1, columnspan=1, pady=10)
Label( #Sub-Header
    frame, 
    text=df, 
    font=("Times", "16")
    ).grid(row=2, columnspan=1, pady=30)



# Buttons
newAccountButton = Button(frame, text="Create New Account", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=newAccount)
newEntryButton = Button(frame, text="New Journal Entry", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=newEntry)
refresh = Button(frame, text="Refresh", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=refreshButton)
ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:ws.destroy())

# Button Grids
newAccountButton.grid(row=3, column=0, pady=20)
newEntryButton.grid(row=3, column=2, pady=20)
refresh.grid(row=3, column=1, pady=20)
ext.grid(row=3, column=3, pady=20)




ws.mainloop()






