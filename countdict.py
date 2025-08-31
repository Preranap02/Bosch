#Write a program to count the frequency of each element in a list.
from collections import Counter
sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = Counter(sample_list)
print(freq)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})