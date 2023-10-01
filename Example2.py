'''
Created on 10. 2. 2018

@author: Hanka
'''
import math

# Simple Example 1
print ("\nSimple Example 1")
print ("a" in "alpha")              # return True
print ("b" in "python")             # return False
print ("a" not in "python")         # return True
print ("b" not in "baby")           # return False


# Simple Example 2
print ("\nSimple Example 2")
number1 = int(input("Enter number1: "))
if (number1 > 5):
    print ("Your number is greater than than 5.") 
else:
    print ("Your number is less than or equal to 5.") 


# Simple Example 3
print ("\nSimple Example 3")
number2 = int(input("Enter number2 for calculation a square root: "))
if (number2 > 0):
    print ("Your number is greater than 0.")
    square_root = math.sqrt(number2)
    print ("Square root %d is %.3f" %(number2, square_root))

else:
    print ("Your number is less than or equal to 0.")
    print ("The square root of a negative number does not exist.")