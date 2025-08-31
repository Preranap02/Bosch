# Write a function to check if a number is even or odd.
def evenorodd(n1):
  if n1%2==0 :
      return "Number is even"
  else : 
      return "Number is odd"
a=int(input("Enter a number "))
print(evenorodd(a))