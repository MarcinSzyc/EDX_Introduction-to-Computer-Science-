# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:40:37 2018

@author: Marcin
"""
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

previousBalance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
minimumMonthlyPayment = 0
remainingBalance = 0

monthlyInterestRate = annualInterestRate / 12


for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
    unpaidBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    previousBalance = unpaidBalanceEachMonth
    
print('Remaining balance: '+ str(round(previousBalance,2)))