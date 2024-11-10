import sys                               #importing the sys module

x = int(input("x: "))   
y = int(input("y: "))

try:                                    #try except method
    result = x / y
       
except ZeroDivisionError:
    print("Can't divide by zero")           
    sys.exit(1)                         #exit the program with an error

print(f"{x} / {y} = {result}")