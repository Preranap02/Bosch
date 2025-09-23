# Write a program to find the factorial of a number
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    return n * factorial(n - 1)   
num=int(input("Enter a number ")) 
print(factorial(num)) 