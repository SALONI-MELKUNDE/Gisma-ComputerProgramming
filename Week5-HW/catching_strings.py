lst1 = [3, 7, 6, 8, 9, "11", 15, 25]
lst2 = []

for num in lst1:
    if isinstance(num, str):
        print("Index [{}] was a string, not an integer".format(lst1.index(num)))
        continue
    lst2.append(num ** 2)

print(lst2)