import sys                               #importing the sys module

try:
    x = int(input("x: "))   
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")        #exception handling for text inputs
    sys.exit(1)
try:                                     #try except method
    result = x / y
       
except ZeroDivisionError:
    print("Can't divide by zero")        #exception handling for division by zero
    sys.exit(1)                          #exit the program with an error

print(f"{x} / {y} = {result}")