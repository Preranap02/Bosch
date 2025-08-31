#Write a program to merge two dictionaries
dict1 = {'apple': 5, 'banana': 3}
dict2 = {'banana': 2, 'orange': 4}
merged = dict1.copy()
for k, v in dict2.items():
    merged[k] = merged.get(k, 0) + v
print(merged)
