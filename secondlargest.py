#Write a function to find the second largest number in a list
def second_largest(numbers):
    if not numbers or len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")

    unique_numbers = set(numbers) 
    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two unique numbers.")

    unique_numbers.remove(max(unique_numbers)) 
    return max(unique_numbers) 
nums = [4, 2, 9, 7, 9, 5]
print(second_largest(nums)) 