'''
Created on 10. 2. 2018

@author: Hanka
'''

print ("\nBasic Calculator\n")

print ("Inputs:")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

total = a + b
difference = a - b
product = a * b 
quotient = a / b

print ("\nResults:")
print ("Total:\t\t", total)
print ("Difference:\t", difference)
print ("Product:\t", product)
print ("Quotient:\t", round(quotient,3))