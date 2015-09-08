balance = float(raw_input("enter balance: "))
annualInterestRate = float(raw_input("enter annual interest rate: "))

mir = annualInterestRate/12.0
mlb = balance/12
mub = (balance*((1+mir)**12))/12.0
bal = 1
fa = 0

while abs(bal) > 0.0001:
		
	fa = (mub + mlb)/2
	bal = balance
	
	for i in range(12):
		m = bal - fa
		bal = m + m*mir
		
	if (bal < 0):
		mub = fa

	elif (bal > 0):
		mlb = fa
		
print "Lowest Payment: ", round(fa,2)