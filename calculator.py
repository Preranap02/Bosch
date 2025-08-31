#Write a program to implement a simple calculator (using +, -, *, /).
def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # Input the operation
    print("Choose operation:")
    print(" +  --> Addition")
    print(" -  --> Subtraction")
    print(" *  --> Multiplication")
    print(" /  --> Division")
    operation = input("Enter operation (+, -, *, /): ")
    result = num1 + num2
    result = num1 - num2
    result = num1 * num2
    result = num1 / num2
    print(result)
calculator()