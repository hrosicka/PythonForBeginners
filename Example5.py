'''
Created on 17. 2. 2018

@author: Hanka
'''

print ("CYCLES AND ARRAYS")
print ("-----------------\n")
number1 = 1
print ("While cycle - all numbers from 0 until <= 10")
while(number1 <= 10):
    print(number1)
    number1 = number1 + 1
    
    
print ("\nEven numbers")
max_number_even = int(input("Enter max number: "))
number2 = 0
while (number2 <= max_number_even):
    if (number2 % 2 == 0):
        print (number2)
    else:
        pass
    number2 = number2 + 1
    

print ("\nOdd numbers")
max_number_odd = int(input("Enter max number: "))
number3 = 0
while (number3 <= max_number_odd):
    if (number3 % 2 == 1):
        print (number3)
    else:
        pass
    number3 = number3 + 1


print ("\nARRAYS")
print ("------\n")
my_array = "Arrays"
print ("All characters in:", my_array)
for i in my_array:
    print (i)


print ("\nNumbers from 0 to 4(including):")    
for i in range(5):
    print (i)
    
print ("\nNumber 3 and 4:")    
for i in range(3,5):
    print (i)
    
print ("\nNumbers 10, 13, 16 and 19:")    
for i in range(10, 20, 3):
    print (i)


print ("\nNumbers 4, 15, 3 and 2:")   
pole = [4, 15, 3, 2]
for i in pole:
    print(i)


print ("\nNumbers 20, 75, 15 and 10:")   
pole = [40, 150, 30, 20]
for i in pole:
    print(i/2)


print ("\nNumbers 80, 300, 60 and 40")   
pole = [40, 150, 30, 20]
for i in pole:
    print(2*i)

input()


    
    