# Write a program to find all prime numbers in a given range. 
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Only check odd factors up to the square root of num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Return a list of prime numbers in the given range [start, end]."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

prime_numbers = find_primes_in_range(start_range, end_range)

print(f"Prime numbers between {start_range} and {end_range}:")
print(prime_numbers)