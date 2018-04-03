# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:40:17 2017

@author: Marcin
"""

balance =3329
newbalance= balance
annualInterestRate = 0.2
fix=10
while True:
    newbalance=balance
    for n in range(12):
        newbalance = (newbalance-fix)*(1+annualInterestRate/12)
    'print(str(balance))'
    if newbalance >0:
        fix+=10
    else:
        break
print('Lowest Payment: '+str(fix))