# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:24:29 2018

@author: Marcin
"""
balance = 3329
annualInterestRate = 0.2
minimumMonthlyPayment = 0
previousBalance = balance
monthlyInterestRate = annualInterestRate / 12



while previousBalance >= 0:
    previousBalance = balance
    minimumMonthlyPayment +=10 
    for i in range(12):
        monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
        unpaidBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        previousBalance = unpaidBalanceEachMonth
    
print('Lowest Payment: '+ str(minimumMonthlyPayment))
