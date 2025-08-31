# Write a program to swap two numbers without using a third variable.
n1=eval(input("Enter a number "))
n2=eval(input("Enter another number "))
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("After swapping")
print("the numbers are " ,n1 ,n2 )
# SIMPLER VERSION
# print("another method")
# n1, n2 = n2, n1;
# print("numbers after swapping",n1 ,n2)