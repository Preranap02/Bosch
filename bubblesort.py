#Write a program to implement bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap if the element found is greater
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
numbers = [64, 25, 12, 22, 11]
sorted_numbers = bubble_sort(numbers.copy())
print("Sorted list:", sorted_numbers)