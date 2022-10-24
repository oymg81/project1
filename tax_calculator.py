# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:11:30 2022

@author: oymg81
"""

#"TAX CALCULATOR"

gross_inc = float(input("Enter your gross income: "))
num_dep = float(input("Enter number of dependents: "))
tax = (gross_inc - 10000)
#Formula
if num_dep > 0 :
    incometax = tax - (num_dep * 3000)
    taxable = incometax *.20
    print("The income tax is:", taxable)
else:
    taxable = tax *.20
print("The income tax is:", taxable)
   