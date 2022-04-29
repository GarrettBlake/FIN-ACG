global debit
global credit

debit = []
credit = []


def d_or_c():
	value = input("Enter d or c. Then hit Enter ")
	if value == "d":
		d = int(input("Enter Debit: "))
		debit.append(d)
	elif value == "c":
		c = int(input("Enter Credit: "))
		credit.append(c)
	else:	
		print("Try Again")
		d_or_c()




def accountBal():
	totalDebit = sum(debit)
	totalCredit = sum(credit)
	netBalance = totalDebit - totalCredit
	if netBalance >= 0:
		print("Debit Balance: ", netBalance)
	else:
		print("Credit Balance: ", netBalance*-1)


