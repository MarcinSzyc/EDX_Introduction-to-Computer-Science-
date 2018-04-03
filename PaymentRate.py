'''Problem 1 - Paying Debt off in a Year'''
'''
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''


balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
MonthlyPaymentLowerBound = balance/12
MonthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12
Guess = (MonthlyPaymentLowerBound + MonthlyPaymentUpperBound)/2
Diff = 0

while True:
    remainingBalance = balance
    for i in range(12):
            remainingBalance = remainingBalance - Guess
            remainingBalance = remainingBalance + (monthlyInterestRate*remainingBalance)
    if abs(remainingBalance) < 0.01:
        break
    elif remainingBalance >0:
        MonthlyPaymentLowerBound = Guess 
    else:
        MonthlyPaymentUpperBound = Guess
    Guess = (MonthlyPaymentLowerBound + MonthlyPaymentUpperBound)/2
print('Lowest Payment: '+str(round((Guess),2)))  