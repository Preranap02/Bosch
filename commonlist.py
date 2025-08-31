#Write a program to find the common elements between two lists.
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return list(common)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Common elements:", common_elements(list1, list2))