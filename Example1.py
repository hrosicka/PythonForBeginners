'''
Created on 10. 2. 2018

@author: Hanka
'''
import math

# Simple Example 1
print ("\nSimple Example 1")
name = input("Hello, what is your name?\n")
property = input ("What is your best property?\n")
print (name, "is", property)

# Simple Example 2
print ("\nSimple Example 2")
number = int(input("Enter number to exponentiate: "))
result = math.pow(number, 2)
print("Result:")
print(number, "^ 2 =", int(result))

# Simple Example 3
print ("\nSimple Example 3")
radius = float(input("Enter radius of circle (cm): "))
perimeter = 2*math.pi*radius
area = math.pi*math.pow(radius,2)
print("Perimeter of circle is: %.3f cm" % perimeter)
print("Area of circle is: %.4f cm^2" % area)