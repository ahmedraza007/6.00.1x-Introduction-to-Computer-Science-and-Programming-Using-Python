balance = float(raw_input("enter balance: "))
annualInterestRate = float(raw_input("enter annual interest rate: "))
monthlyPaymentRate = float(raw_input("enter monthly payment rate: "))

z = 0
for n in range(12):
	minpay = balance*monthlyPaymentRate
	ub = balance - minpay
	mir = annualInterestRate/12.0
	i = ub*mir
	fb = ub + i
	z = z + minpay
	print '\n'
	print "Month: ", n+1
	print "Minimum monthly payment:", round(minpay,2)
	print "Remaining balance: ", round(fb,2)
	balance = fb
	if (n+1) == 12:
		print '\n'
		print "total Paid", round(z,2)
		print "remaining balance", round(fb,2)