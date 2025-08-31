#Write a function that accepts **kwargs and returns the sum of values.
def sum_kwargs(**kwargs):
    total = sum(kwargs.values())
    return total
result = sum_kwargs(a=10, b=20, c=30)
print(f"The sum of values is: {result}")