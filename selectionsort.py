#Write a program to sort a list without using built-in sort()
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print("Sorted list (Selection Sort):", sorted_numbers)