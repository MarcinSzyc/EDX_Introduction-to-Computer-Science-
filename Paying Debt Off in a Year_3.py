# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:58:13 2018

@author: Marcin
"""
balance = 320000
annualInterestRate = 0.2
previousBalance=0
monthlyInterestRate = annualInterestRate / 12
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance*((1 + monthlyInterestRate)**12))/12
test=balance


while test > 0.1:
    if previousBalance < 0:
        monthlyPaymentUpperBound = minimumMonthlyPayment
    elif previousBalance >0:
        monthlyPaymentLowerBound = minimumMonthlyPayment
    previousBalance = balance
    minimumMonthlyPayment = round((monthlyPaymentUpperBound + monthlyPaymentLowerBound)/2,2)
    for i in range(12):
        monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
        unpaidBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        previousBalance = unpaidBalanceEachMonth
    test = balance - (balance-abs(previousBalance))
print('Lowest Payment: ' + str(minimumMonthlyPayment))
