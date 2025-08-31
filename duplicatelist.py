#Write a program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
inlist=input("Enter list without space")
#my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(inlist))