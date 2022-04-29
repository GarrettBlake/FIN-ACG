import balancefunc
from balancefunc import d_or_c
from balancefunc import accountBal

x = True

while x == True:
	d_or_c()
	end = input("end?")
	if end == "end":
		accountBal()
		quit()
	else:
		continue
