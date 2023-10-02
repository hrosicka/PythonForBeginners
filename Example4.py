'''
Created on 11. 2. 2018

@author: Hanka
'''


print ("CALCULATOR\n")

repeat_calculation = True

while repeat_calculation:

    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    
    print ("Operation Numbers")
    print ("1 - total")
    print ("2 - difference")
    print ("3 - product")
    print ("4 - quotient")

    
    math_operation = int(input("Enter Operation Number: "))
    
    if (math_operation == 1):
        print ("%d + %d = %d" %(a, b, a+b))
        
    elif (math_operation == 2):
        print ("%d - %d = %d" %(a, b, a-b))
        
    elif (math_operation == 3):
        print ("%d * %d = %d" %(a, b, a*b))
        
    elif (math_operation == 4):
        print ("%d / %d = %.1f" %(a, b, a/b))
        
    else:
        print ("Invalid choice")
        
    repeat_calculation = int(input("Do you want to continue? [yes = 1, no = 0]: "))
    
input("\nPress any key...")
