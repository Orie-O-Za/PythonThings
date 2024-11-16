from function import *

while True:
    print("what do you want to do?")
    print("  ")
    print("1 - Addition")
    print("2 - Substraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("Press the Q Key to Close The Calculator")

    if choice == 'q' or 'Q':
        break

    choice = input("Enter your option : ")

    num1 = float(input("Enter the 1st number:  "))
    num2 = float(input("Enter the 2nd number:  "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtration(num1,num2)
    elif choice == '3':
        multiplication(num1,num2)
    elif choice == '4':
        divisioni(num1,num2)
    else:
        print("Invalid Choice")