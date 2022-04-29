from tkinter import *
import re
from tkinter import messagebox
import random
import sqlite3
import os
import pandas as pd


def createAccount():
    wsca = Tk()
    wsca.title('ACG - Create Account')
    wsca.geometry('500x400')
    wsca.config(bg="#447c84")
    wsca.attributes('-fullscreen',False)
    
    # frames
    frame = Frame(wsca, padx=20, pady=20)
    frame.pack(expand=True)
    


    def submit():
        number = accountNumber.get()
        name = accountName.get()
        balance = balanceType.get()
        valuation = valuationType.get()
        correlation = correlatedAccount.get()

        combiner = str(number) +"_"+ str(name)
        inserter = "'"+str(number)+"'" +","+"'" +str(name)+"'" +","+"'" +str(balance)+"'" +","+"'" +str(valuation)+"'" +","+"'" +str(correlation)+"'"+","+"'" +str(valuation) +"')"

        con = sqlite3.connect('AccountData/'+str(combiner)+'.db')
        cur = con.cursor()

        cur.execute('CREATE TABLE '+str(name)+'(AccountNumber real, AccountName text, BalanceType text, NetBalance real, ValuationAccount text, CorrelatedAccount text)')
        cur.execute('CREATE TABLE Transactions (transactionID real, dated date, debit real, credit real, description text)')
        cur.execute("INSERT INTO "+str(name)+" VALUES (" + inserter)

        
        con.commit()
        con.close()

        accountNumber.delete(0, END)
        accountName.delete(0, END)
        balanceType.delete(0, END)
        valuationType.delete(0, END)
        correlatedAccount.delete(0, END)
        


    
    # labels
    Label(
        frame, 
        text='Account Creator', 
        font=("Times", "24", "bold")
        ).grid(row=0, columnspan=3, pady=10)
    
    Label(
        frame, 
        text="Account Number: ",
        font=("Times", "14")
        ).grid(row=1, column=0, pady=5)

    Label(
        frame, 
        text="Account Name: ",
        font=("Times", "14")
        ).grid(row=2, column=0, pady=5)

    Label(
        frame, 
        text='Balance Type: ', 
        font=("Times", "14")
        ).grid(row=3, column=0, pady=5)
    
    Label(
        frame, 
        text='Valuation Type: ', 
        font=("Times", "14")
        ).grid(row=4, column=0, pady=5)
       
    Label(
        frame, 
        text='Correlated Account: ', 
        font=("Times", "14")
        ).grid(row=5, column=0, pady=5)

    # Entry
    accountNumber = Entry(frame, width=30)
    accountName = Entry(frame, width=30)
    balanceType = Entry(frame, width=30)
    valuationType = Entry(frame, width=30)
    correlatedAccount = Entry(frame, width=30)

    accountNumber.grid(row=1, column=1)
    accountName.grid(row=2, column=1)
    balanceType.grid(row=3, column=1)
    valuationType.grid(row=4, column=1)
    correlatedAccount.grid(row=5, column=1)
    

    # button 
    reg = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)
    ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:wsca.destroy())
    reg.grid(row=6, column=1, pady=20)
    ext.grid(row=6, column=2, pady=20)
    

    
    
    wsca.mainloop()
