from functions import *

while True:
    print("what do you want to do?")
    print("  ")
    print("1 - Addition")
    print("2 - Substraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("Press the Q Key to Close The Calculator")

    choice = input("Enter your option : ")

    num1 = float(input("Enter the 1st number:  "))
    num2 = float(input("Enter the 2nd number:  "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multiplication(num1,num2)
    elif
        choice == '4':
        division(num1,num2)
    else:
        print("Invalid Choice")