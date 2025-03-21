from pycparser.c_ast import While


def Sum():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a+b)

def subtraction():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a-b)

def Multiply():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a*b)

def divide():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a/b)

on = True
while on:
    x = input("Please Enter a valid operation +, -, * or /\n")
    if x == '+':
        Sum()
        break
    elif x == '-':
        subtraction()
        break
    elif x == '*':
        Multiply()
        break
    elif x == '/':
        divide()
        break
    else:
        print("The operation You entered is invalid")
        break
