#Write a program to rotate a list by k positions
def rotate_list(lst, k):
    n = len(lst)
    if n == 0:
        return lst
    k = k % n
    rotated = lst[-k:] + lst[:-k]
    return rotated

my_list = input("Enter list numbers")
k = int(input("value of k"))

rotated_list = rotate_list(my_list, k)
print("Original list:", my_list)
print(f"List rotated by {k} positions:", rotated_list)