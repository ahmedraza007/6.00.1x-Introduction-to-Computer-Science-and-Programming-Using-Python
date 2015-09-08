balance = float(raw_input("enter balance: "))
annualInterestRate = float(raw_input("enter annual interest rate: "))

mir = annualInterestRate/12.0
fa = 0
bal = 1

while bal > 0:
	fa = fa + 10
	bal = balance
	
	for i in range(12):
		mub = bal - fa
		bal = mub + mir*mub
		
print "Lowest Payment: ", fa