import sys

y = int(input("y: "))
x = int(input("x: "))   
try:
    result = x / y
       
except ZeroDivisionError:
    print("Can't divide by zero")           
    sys.exit(1) 

print(f"{x} / {y} = {result}")